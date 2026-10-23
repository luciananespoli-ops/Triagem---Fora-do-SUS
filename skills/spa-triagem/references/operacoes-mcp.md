# Contrato operacional do MCP SPA

Usar o conector SPA MCP — Triagem, sem criar cliente alternativo ou acessar cookies. Conferir o schema disponível na sessão. Os nomes abaixo são nomes funcionais; o conector pode acrescentar prefixos.

| Ferramenta | Uso e parâmetros relevantes |
|---|---|
| `listar_expedientes_triagem` | `caixa`, `limite`, `pagina`; retorna identidades, PDFs e pendências da página. Não toma ciência. |
| `ler_expediente_triagem` | `caixa`, `procedure_id`, `expediente_id`; PDFs, páginas, duplicatas e falhas. |
| `inspecionar_formulario_triagem` | Mesma identidade; campos/opções atuais. Abre formulário, não salva. |
| `preparar_triagem` | Identidade + valores abaixo; preenche, não salva. |
| `salvar_classificacao_triagem` | Identidade + valores abaixo; preenche, envia e confere novo evento. |
| `inspecionar_encerramento` | Identidade; abre/lê formulário, não sugere encerramento por si só. |
| `salvar_sugestao_encerramento` | Identidade; registra sugestão com Outros, sem criar Ofício. |
| `inspecionar_lote_ciencia` | `caixa`; reúne candidatos com botão em todas as páginas, sem iniciar prazo. |
| `tomar_ciencia_expediente` | `caixa`, `procedure_id`, `expediente_id`, `processo`, `autorizar_inicio_prazo=true`; inicia prazo. |
| `tomar_ciencia_caixa` | `caixa`, `autorizar_inicio_prazos=true`; nova seleção da caixa e execução longa; considerar restrições abaixo. |

## Valores de classificação

Fornecer explicitamente:

- `manifestacao_codigo`, `manifestacao_nome`, `observacao`;
- `assessor=""` em todas as classificações, mantendo o campo vazio;
- `usuario_oficio`, `observacao_oficio`, `vencimento_oficio` para criar Ofício;
- não preencher destinatário sem tarefa nem passar data de teste fixa.

O botão que envia a classificação chama-se **Complementar classificação do processo**. A ferramenta de salvar corresponde a esse envio, não ao botão de sugestão de encerramento.

## Limites atuais relevantes

- A extensão compartilha uma aba SPA. Serializar todas as chamadas; não abrir sessões paralelas para acelerar.
- O MCP foi configurado para fila `user_id=527`, fluxo 42, FSUS 605 e IP 606. Isso não é o ID do usuário autenticado nem autorização para personificar essa pessoa. Não alegar que a fila pertence a um novo usuário sem validação.
- A listagem normal pode rejeitar linhas sem PDF e colocá-las em `pendencias`. A inspeção de ciência encontra botões mesmo nessas linhas. Não exigir que uma linha sem ciência conste de `expedientes` para identificá-la pela ferramenta própria.
- Uma página pode ter agrupamentos sem células; não confundir esses grupos com expedientes.
- Marcadores de tentativa persistem no navegador do computador onde a extensão roda. Não são controle de concorrência compartilhado entre computadores. Não executar dois computadores ao mesmo tempo usando o mesmo túnel.
- O lote de ciência atual foi testado com timeouts: algumas ações só puderam ser confirmadas depois, e outras exigiram conferência manual. Não repetir mutação só porque houve timeout.
- `tomar_ciencia_caixa` refaz a seleção: pode incluir entradas posteriores à inspeção. Para executar uma lista aprovada, preservar as identidades e usar chamadas individuais. Não declarar que existe token de snapshot ou filtro de IDs no schema atual.
- Uma chamada longa pode exceder o tempo do cliente/túnel. Não aumentar timeout nem repetir mutações para contornar; executar individualmente e conferir cada resultado.
- Se a conexão cair, reportar exatamente em que expediente houve interrupção e consultar o estado antes de retomar. Não apagar `localStorage` para liberar nova tentativa.
- Não há leitura automática de PDFs digitalizados por OCR, uso automático do PJe, criação de agravo ou geração de minutas nesta integração.

## Saída recomendada

Para uma consulta/análise: processo, expediente, documento/página, síntese, providência proposta e pendências. Para execução: identidade, ação, confirmação do SPA, evento quando retornado e falhas. Resumir volumes e destacar somente itens que exigem intervenção; evitar transcrever todos os PDFs sem pedido.

Distinguir sempre **preparado**, **salvo e confirmado**, **sugestão de encerramento registrada**, **ciência confirmada operacionalmente no SPA** e **resultado incerto**. Não tratar esses estados como equivalentes.
