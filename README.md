# Triagem + Assistente de Minutas

Fontes do plugin `triagem-assistente-minutas`, versão **0.9.6**, importados do pacote `plugin (14).zip`.

## Estrutura

- `plugin.json`: manifesto portátil.
- `.codex-plugin/plugin.json`: manifesto de compatibilidade Codex.
- `.app.json`: referência à conexão existente do aplicativo; não contém credenciais.
- `skills/fluxo-triagem-minutas/`: skill de coordenação, configuração de interface e referências.
- `ATUALIZACAO-COREPLAN-0.9.5.md`: histórico fornecido no pacote. As versões mencionadas nesse histórico são anteriores à versão dos manifestos.

## Atualizações

Edite os arquivos neste repositório e revise as diferenças antes de enviar as mudanças ao GitHub. Ao lançar uma nova versão, mantenha nome e versão concordantes nos dois manifestos.

Para gerar um pacote a partir dos arquivos versionados, após registrar as mudanças em um commit:

```sh
git archive --format=zip --output=/tmp/triagem-assistente-minutas-plugin.zip HEAD plugin.json .codex-plugin/plugin.json .app.json skills ATUALIZACAO-COREPLAN-0.9.5.md
```

Depois, atualize ou reinstale o pacote pelo fluxo de instalação do plugin na conta e confira a versão em uma nova conversa. Este repositório não configura sincronização automática nem publicação do plugin instalado. Publicar o ambiente de desenvolvimento na nuvem também não publica o plugin.

## Dependências e limites

O pacote contém instruções e referências; não há aplicação executável, dependências para instalar ou suíte de testes. O servidor MCP Triagem, a extensão Chrome, as skills jurídicas específicas e as conexões Google Drive/Docs são dependências externas e não estão incluídos. O identificador em `.app.json` referencia um aplicativo existente e não instala seu servidor.

As instruções jurídicas da skill são conteúdo do plugin: importar ou atualizar estes arquivos não autoriza executar ações em processos ou minutas.
