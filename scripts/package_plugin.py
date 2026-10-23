"""Validate and package the committed plugin, without external dependencies."""

import io
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile


def build(output):
    root = Path(__file__).resolve().parents[1]
    archive = subprocess.check_output(
        ["git", "archive", "--format=zip", "HEAD", "plugin.json",
         ".codex-plugin/plugin.json", "assets", "skills"],
        cwd=root,
    )
    with zipfile.ZipFile(io.BytesIO(archive)) as package:
        names = set(package.namelist())
        documents = {
            name: json.loads(package.read(name))
            for name in names if name.endswith(".json")
        }
        portable = documents["plugin.json"]
        legacy = documents[".codex-plugin/plugin.json"]
        for key in ("name", "version", "description"):
            if portable[key] != legacy[key]:
                raise ValueError(f"Manifestos divergem: {key}")
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", portable["version"]):
            raise ValueError("Versão deve seguir major.minor.patch")
        if legacy["skills"] != "./skills":
            raise ValueError("Diretório de skills inesperado")
        interface = portable["extensions"]["com.openai"]["interface"]
        if interface != legacy["interface"]:
            raise ValueError("Interfaces dos manifestos divergem")
        for key in ("logo", "composerIcon"):
            path = interface[key].removeprefix("./")
            if path not in names:
                raise ValueError(f"Ícone ausente: {path}")
        skills = sorted(n for n in names if n.startswith("skills/") and n.endswith("/SKILL.md"))
        if not skills:
            raise ValueError("Nenhuma skill incluída")
        for skill in skills:
            text = package.read(skill).decode("utf-8")
            if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
                raise ValueError(f"Metadados ausentes: {skill}")
        if package.testzip() is not None:
            raise ValueError("ZIP corrompido")
    output = Path(output).resolve()
    if output.is_relative_to(root):
        raise ValueError("Grave o pacote fora do checkout, por exemplo em /tmp")
    output.write_bytes(archive)
    print(f"Plugin {portable['name']} {portable['version']}: {len(skills)} skill(s); pacote: {output}")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "/tmp/triagem-spa-fsus-ip-plugin.zip")
