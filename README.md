# Triagem SPA — FSUS e IP 2.0

Fontes do plugin `triagem-spa-fsus-ip`, versão de manifesto **0.1.1**, importadas da release `pluginrel_6adbcee3dce48191b0d64a361d9d4a4a`. “2.0” integra o nome exibido do plugin.

Este pacote substitui o antigo Triagem + Assistente de Minutas. Os arquivos anteriores permanecem no histórico Git.

## Estrutura

- `plugin.json` e `.codex-plugin/plugin.json`: manifestos originais do plugin.
- `assets/`: ícone do plugin.
- `skills/spa-triagem/`: triagem SPA e referências integrais.
- `skills/orquestrar-triagem-spa/`: coordenação geral e contrato do relatório.
- `skills/orquestrar-triagem-fsus/` e `skills/orquestrar-triagem-ip/`: coordenação por caixa.
- `skills/indicar-modelos-peticoes-cdsp/`: indicação com catálogo de 72 registros.
- `skills/indicar-modelos-internacao-acolhimento-cdsp/`: indicação com catálogo de 21 registros.

## Atualizações e pacote

A branch **`main` é a fonte oficial do plugin**. Alterações podem ser propostas em branches e pull requests para `main`. Mantenha os dois manifestos concordantes.

A cada envio à `main`, o GitHub Actions executa **Pacote do plugin (main)**: valida os JSONs, a concordância dos manifestos, os ícones e a presença das skills, e gera um ZIP do commit exato. Pull requests para `main` também são validados, sem disponibilizar pacote oficial.

Para baixar, abra **Actions → Pacote do plugin (main)** e escolha a execução bem-sucedida do commit mais recente de `main`. Baixe `triagem-spa-fsus-ip-main-<SHA>` e extraia o ZIP interno `triagem-spa-fsus-ip-plugin.zip`. Os artefatos ficam disponíveis por 90 dias. Também é possível executar **Run workflow** selecionando `main`.

Para gerar localmente, após registrar as mudanças em um commit:

```sh
python3 scripts/package_plugin.py /tmp/triagem-spa-fsus-ip-plugin.zip
```

O script empacota os arquivos de `HEAD`. Publicação e instalação na conta são etapas separadas; alterar este repositório não atualiza o plugin instalado automaticamente.

## Dependências e limites

O conector **SPA MCP — Triagem** deve estar disponível separadamente. O pacote não instala extensão, servidor ou conexão; por isso, não inclui a antiga referência `.app.json`.

As seis skills coordenam triagem FSUS/IP e recomendação de modelos a partir do relatório. A indicação não seleciona modelos no SPA nem preenche minutas. Importar estes arquivos não autoriza ações em processos.

As verificações de empacotamento são estruturais: não executam o fluxo jurídico nem validam conexões externas.
