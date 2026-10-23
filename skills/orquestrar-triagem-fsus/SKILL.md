---
name: orquestrar-triagem-fsus
description: Coordenar exclusivamente a caixa FSUS no SPA, aplicar a skill de triagem
  original e encaminhar seu relatório à indicação de modelos CDSP.
---

# Orquestrador FSUS — Fora do SUS

1. Fixar CAIXA_ALVO=FSUS apenas quando o pedido ou a escolha vigente identificar esta caixa. Se o usuário mencionar outra caixa, retornar ao [orquestrador geral](../orquestrar-triagem-spa/SKILL.md). Não trocar a caixa por iniciativa própria.
2. Ler integralmente [spa-triagem](../spa-triagem/SKILL.md), suas referências comuns analise-juridica.md, regras-triagem.md e operacoes-mcp.md e somente o [módulo FSUS](../spa-triagem/references/fsus.md). Não carregar o módulo da outra caixa.
3. Aplicar todas as restrições da skill original: hipóteses aprovadas, assessor em branco, observações específicas, Ofícios condicionais, ciência separada, confirmações expressas por hipótese, códigos atuais e conferência de eventos. Não presumir que códigos ou salvamentos de outra caixa foram validados aqui.
4. Executar leitura, análise, preparação ou gravação estritamente no modo autorizado e sequencialmente. Não repetir mutação após resultado incerto sem consultar o estado.
5. Produzir o relatório obrigatório por expediente. Cumprir o [contrato de integração](../orquestrar-triagem-spa/references/contrato-relatorio-modelos.md) para encaminhar os dados à [indicadora CDSP](../indicar-modelos-peticoes-cdsp/SKILL.md). Se a integração já foi feita pela skill original, reutilizar seu resultado sem repeti-la.
6. A competência da caixa não garante modelo compatível no catálogo de 72 registros. Não importar catálogos de outros plugins nem adaptar modelo incompatível. Conservar os nomes literais e as pendências da indicação.
7. Reportar separadamente análise, gravação confirmada, sugestão de encerramento, pendência, resultado incerto e indicação de modelo. A ausência de modelo não desfaz classificação válida; uma indicação não autoriza gravação nem supre regra ausente.
