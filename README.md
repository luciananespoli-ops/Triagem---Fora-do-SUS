# Triagem + Assistente de Minutas

Fontes do plugin `triagem-assistente-minutas`, versão **0.9.8**, importados do pacote `plugin (14).zip`.

## Estrutura

- `plugin.json`: manifesto portátil.
- `.codex-plugin/plugin.json`: manifesto de compatibilidade Codex.
- `.app.json`: referência à conexão existente do aplicativo; não contém credenciais.
- `skills/fluxo-triagem-minutas/`: skill de coordenação, configuração de interface e referências.
- `ATUALIZACAO-COREPLAN-0.9.5.md`: histórico fornecido no pacote. As versões mencionadas nesse histórico são anteriores à versão dos manifestos.

## Atualizações

A branch **`main` é a fonte oficial do plugin**. Você e Burno podem trabalhar em branches e abrir pull requests para `main`, ou enviar alterações diretamente a ela quando apropriado. Atualizações que permaneçam em outra branch não integram o pacote oficial. Ao lançar uma nova versão, mantenha nome e versão concordantes nos dois manifestos.

A cada envio à `main`, o GitHub Actions executa **Pacote do plugin (main)**: valida os JSONs, a concordância dos manifestos e a presença das skills, e gera um ZIP do commit exato. Pull requests para `main` também são validados, sem disponibilizar um pacote oficial. Essas verificações são estruturais; não executam o fluxo jurídico nem validam conexões externas.

Para baixar: abra **Actions → Pacote do plugin (main)**, escolha a execução bem-sucedida do commit mais recente de `main` e baixe o artefato `triagem-assistente-minutas-main-<SHA>`. O GitHub entrega um arquivo compactado contendo `triagem-assistente-minutas-plugin.zip`; extraia o ZIP interno para instalar. Os artefatos ficam disponíveis por 90 dias. Se necessário, execute novamente pela opção **Run workflow**, selecionando `main`. O GitHub Actions precisa estar habilitado no repositório.

Para gerar um pacote a partir dos arquivos versionados, após registrar as mudanças em um commit:

```sh
python3 scripts/package_plugin.py /tmp/triagem-assistente-minutas-plugin.zip
```

Depois, atualize ou reinstale o pacote pelo fluxo de instalação do plugin na conta e confira a versão em uma nova conversa. A geração do pacote acompanha automaticamente a `main`; a publicação e a instalação na conta continuam separadas. Publicar o ambiente de desenvolvimento na nuvem também não publica o plugin.

## Dependências e limites

O pacote contém instruções e referências; não há aplicação executável, dependências para instalar ou suíte de testes. O servidor MCP Triagem, a extensão Chrome, as skills jurídicas específicas e as conexões Google Drive/Docs são dependências externas e não estão incluídos. O identificador em `.app.json` referencia um aplicativo existente e não instala seu servidor.

As instruções jurídicas da skill são conteúdo do plugin: importar ou atualizar estes arquivos não autoriza executar ações em processos ou minutas.

## Indicação após a triagem

O fluxo emite primeiro o relatório de triagem e um pacote de evidências para a skill indicadora, conforme `skills/fluxo-triagem-minutas/references/indicacao-modelos.md`. O relatório interno de preenchimento continua posterior à confirmação do modelo. O pacote inclui a skill `indicar-modelos-peticoes-cdsp` e seu catálogo original de 72 registros. Instale a versão atualizada para disponibilizar as duas skills na sessão.

## Internação e acolhimento

Inclui `indicar-modelos-internacao-acolhimento-cdsp`, com os 21 registros do inventário fornecido, e roteamento pelo objeto da triagem. Preserva diferenças de modalidade, idade, fase, recurso e omissão, bem como duplicidades e ressalvas do inventário. Indicação não equivale a preenchimento: modelos sem skill específica permanecem com execução pendente.
