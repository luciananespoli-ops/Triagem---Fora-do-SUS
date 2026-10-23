---
name: orquestrar-triagem-spa
description: Coordenar triagem SPA FSUS ou IP e encaminhar o relatório para indicação
  de modelos CDSP, mantendo autorização e execução sequencial.
---

# Orquestrador geral — Triagem SPA

## Roteamento

1. Pedido somente de indicação com relatório pronto: rotear pelo objeto expresso: Fora do SUS usa [Indicar Modelos de Petições — CDSP](../indicar-modelos-peticoes-cdsp/SKILL.md), com 72 registros; internação psiquiátrica ou acolhimento institucional usa [Indicar Modelos de Internação Psiquiátrica e Acolhimento Institucional — CDSP](../indicar-modelos-internacao-acolhimento-cdsp/SKILL.md), com 21 registros. Não consultar SPA nem iniciar triagem. Em objetos mistos, analisar separadamente cada pedido no catálogo correspondente; se o objeto estiver indefinido, pedir o esclarecimento necessário. Se faltar relatório, solicitar o relatório conforme a skill indicadora.
2. Pedido de triagem: definir uma única CAIXA_ALVO antes de chamar ferramentas. Se não houver caixa explícita ou vigente, perguntar FSUS ou IP e aguardar. Não escolher FSUS por padrão. Se o usuário pedir as duas caixas expressamente, executar uma após a outra, com relatórios separados.
3. FSUS: usar [orquestrador FSUS](../orquestrar-triagem-fsus/SKILL.md). IP: usar [orquestrador IP](../orquestrar-triagem-ip/SKILL.md). Estes são módulos de instruções executados na mesma sessão; não requerem agentes simultâneos.
4. Respeitar consulta, preparação, execução e ciência da skill original. Este plugin não amplia permissões nem substitui confirmação expressamente exigida por hipótese específica. Criar ou instalar o plugin não autoriza acessar processos ou gravar no SPA.

## Integração e limites

- Aplicar integralmente [spa-triagem](../spa-triagem/SKILL.md) e suas referências. Regras específicas aprovadas que expressamente substituem orientações anteriores prevalecem sobre exemplos genéricos; não reescrever regras jurídicas na orquestração. Conflito sem precedência expressa: sinalizar a pendência, sem inventar regra.
- As ferramentas do conector SPA MCP — Triagem precisam estar disponíveis separadamente. Descobrir os schemas atuais; nomes semelhantes em Triagem Terapia não comprovam equivalência. Não substituir o conector por ferramentas de outra integração nem migrar filas, sessão ou credenciais automaticamente.
- Se o conector ou uma ferramenta necessária não estiver disponível, informar exatamente a operação impedida. Continuar análise de documentos já fornecidos e indicação por relatório pronto quando possível. Não afirmar execução no SPA nem teste real.
- Consultar MCP PJe somente nas condições e hipóteses da skill original. Não inventar endpoint nem considerar uma conexão de PJe testada por instalar este plugin.
- Toda interação SPA é sequencial. Preservar caixa + processo + procedure_id + expediente_id. Não deduplicar pelo CNJ nem executar caixas simultaneamente.
- Após produzir o relatório de cada expediente, seguir o [contrato de integração](references/contrato-relatorio-modelos.md) e usar a skill indicadora, quando houver providência processual definida. Não executar duas vezes esta integração se spa-triagem já a concluiu.
- Não selecionar modelos no SPA, emitir ou preencher minutas, criar documentos, redistribuir processos ou iniciar ciência em consequência da indicação.
- Ao final, manter os três blocos obrigatórios por expediente, a indicação separada e os totais/pendências exigidos pela triagem. Pedido somente de indicação mantém exclusivamente o formato da skill indicadora.
