# Regras comuns de automação da triagem

## Análise e execução

Analisar os PDFs com o ChatGPT; usar o MCP para obter dados, selecionar opções e gravar. Não delegar a análise ao painel Gemini. Preservar a mesma identidade composta em todas as etapas. O MCP executa valores explícitos; não escolhe a providência jurídica.

Os critérios jurídicos da antiga habilidade Triagem do Gemini estão em [analise-juridica.md](analise-juridica.md). Aplicá-los diretamente no GPT; não invocar Gemini. Distinguir recomendação jurídica de execução disponível no MCP.

## Assessor em branco — todas as manifestações

Deixar o campo Assessor em branco em todas as hipóteses de manifestação, tanto em FSUS quanto em IP. Não selecionar nomes nem reutilizar assessor sugerido pelo SPA ou pelo cabeçalho IA. Enviar `assessor=""` nas ferramentas de classificação e conferir o campo vazio antes de salvar. As regras antigas de distribuição ficam suspensas; a designação será definida futuramente pelo usuário. A ausência de regra de distribuição não impede executar uma hipótese de manifestação já aprovada.

Manter preenchida a observação destinada ao assessor conforme cada hipótese. O usuário da tarefa de Ofício é campo distinto: continuar designando YASMIM MARQUES NASCIMENTO quando a regra exigir Ofício.

## Observação do processo

Usar obrigatoriamente: `[PREFIXO] - [ORIENTAÇÃO RESUMIDA] - Triagem automatizada`.

- PREFIXO = FSUS ou IP, de acordo com a caixa selecionada.
- Produzir orientação curta e fiel à análise; não copiar a análise completa.
- Exemplos: `FSUS - Apresentar contestação / Liminar indeferida - Triagem automatizada`; `IP - Apresentar impugnação ao cumprimento de sentença - Triagem automatizada`.
- Substituir o padrão dos testes anteriores “Triagem automatizada por IA / ...” por este formato, conforme o prompt atual.
- Recomendar agravo na orientação, quando fundamentado, não autoriza criar tarefa de Agravo de instrumento: eventual tarefa cabe ao assessor depois. Manter o campo Assessor em branco.

## Tarefa condicional de Ofício

Criar tarefa somente quando a análise e as regras aplicáveis indicarem expressamente sua necessidade. Não criar Ofício em todo expediente por padrão.

| Campo | Regra |
|---|---|
| Tipo da tarefa | Ofício; confirmar a opção efetivamente selecionada |
| Usuário da tarefa | YASMIM MARQUES NASCIMENTO, nome completo e seleção exata |
| Vencimento | Próximo dia de segunda a sexta posterior à criação; pular apenas sábados e domingos |
| Prazo em dias úteis | Em branco |
| Observação da tarefa | Finalidade/tipo de Ofício recomendado, separada da observação geral |

Yasmim substitui o nome Enzo do prompt antigo, por confirmação expressa do usuário. Não atribuir Ofícios a Enzo. A tarefa não precisa ser atribuída ao mesmo assessor do processo.

Calcular a data em America/Cuiaba imediatamente antes de salvar. Segunda vence terça; terça vence quarta; quarta vence quinta; quinta vence sexta; sexta/sábado/domingo vencem na segunda seguinte. Não descontar feriados, conforme confirmação atual do usuário, mesmo que o prompt antigo mencione feriados. Preservar passagem de mês/ano. Usar `dd/mm/aaaa`. Não tratar essa data de tarefa interna como prazo processual.

Se uma orientação atual do usuário fornecer data específica, aplicá-la como exceção documentada para o escopo indicado. Não inventar data atribuída ao Gemini. Se a data conflitar com o pedido, esclarecer o conflito antes da gravação.

## Opções conhecidas: conferir no formulário

- Yasmim no usuário da tarefa de Ofício: `1440`. Validar por nome e código atuais; manter Assessor em branco.
- Tipo Ofício: `OPT040516`.
- Contestação no fluxo FSUS validado: `OPT032695`. Há outra opção “Contestação”, `OPT037920`, que não foi selecionada pelo usuário; não escolher pela posição.
- Não presumir códigos de outras manifestações ou de IP. Inspecionar as opções atuais. Se houver uma única opção exata e inequívoca, usar o código retornado; se houver duplicidade não resolvida, pedir definição.
- Não usar “Manifestação” (`OPT040586`) como preenchimento genérico para qualquer ato.

## Sugestão de encerramento

Aplicar as hipóteses de encerramento expressamente previstas em analise-juridica.md, sem generalizar para todo acórdão ou ato favorável. Embargos de Declaração nunca autorizam sugestão de encerramento por esta skill.

Quando houver regra/decisão explícita do usuário e autorização para sugerir encerramento, manter “Outros” (`OPT041489`) e o encaminhamento fornecido pelo SPA, sem alterar procuradores por iniciativa própria. A necessidade de Ofício continua independente; não supor que sugerir encerramento cria a tarefa. Verificar as limitações de composição no contrato MCP.

## Regra de contestação validada em 15/10/2026

Esta orientação atual prevalece sobre critérios anteriores conflitantes dos módulos e da matriz:

- Confirmar Contestação quando o PDF contiver comando atual “Cite-se” ou “Citem-se” dirigido ao Estado de Mato Grosso e a pretensão for de competência de Fora do SUS ou Internação Psiquiátrica. Conferir o destinatário e a competência pelo documento completo; não usar trecho de precedente ou citação dirigida somente a outro réu.
- Havendo liminar deferida, registrar “Liminar deferida. Possível agravo de instrumento.” na observação do processo. Não avaliar cabimento de agravo neste fluxo nem criar tarefa de agravo.
- Confirmada a contestação sem multa pertinente ao Estado e sem responsabilidade secundária estadual (ver regra SECUND abaixo), criar Ofício com observação exatamente: `Enviar ofício "CUMP GERAL" - Cumprimento de decisão judicial.` Preservar o ponto final. Esta regra substitui a seleção anterior de SINF para contestação sem multa.
- Para todo Ofício, selecionar YASMIM MARQUES NASCIMENTO e o dia seguinte à criação em America/Cuiaba, avançando até segunda-feira quando cair sábado ou domingo. Não considerar feriados; deixar prazo em dias úteis vazio.
- Deixar Assessor em branco em toda Contestação, inclusive APLV, conforme a regra comum atual.
- Incluir sempre a informação “Triagem automatizada 🤖” na observação destinada ao assessor (observação do processo), separadamente da observação da tarefa de Ofício. Para citação com liminar deferida, usar `[PREFIXO] — Liminar deferida. Possível agravo de instrumento. Triagem automatizada 🤖.`, com prefixo FSUS ou IP conforme a caixa. Redação validada em 15/10/2026; substitui a redação anterior sem essa informação. Não preencher o seletor de Assessor apenas por atualizar essa observação.
- A autorização desse expediente não autoriza executar outros processos da lista; continuar revisão individual conforme solicitação do usuário.

## Contestação + SECUND — FSUS e IP

Aplicar a todos os casos de competência de Fora do SUS ou Internação Psiquiátrica em que esteja confirmada a citação do Estado para Contestação e a decisão atribua cumprimento primário a outro ente, com responsabilidade secundária do Estado. Esta regra específica prevalece sobre CUMP GERAL nessa hipótese.

- Selecionar manifestação Contestação.
- Alterar somente a redação da observação da tarefa de Ofício para exatamente: `Enviar ofício "SECUND" - Responsabilidade secundária ao Estado.` Preservar o ponto final.
- Manter tipo Ofício, destinatária YASMIM MARQUES NASCIMENTO e vencimento no dia seguinte à criação em America/Cuiaba, pulando somente sábados e domingos, sem considerar feriados; prazo em dias úteis vazio.
- Havendo liminar deferida, manter a observação do processo `[PREFIXO] — Liminar deferida. Possível agravo de instrumento. Triagem automatizada 🤖.`, usando FSUS ou IP conforme a caixa. Não avaliar cabimento de agravo neste fluxo nem criar tarefa de agravo.
- Deixar Assessor em branco também em Contestação + SECUND.
- O processo 1066642-21.2026.8.11.0041 é o exemplo validado: cumprimento primário do Município de Sinop e secundário do Estado. A autorização atual é para salvar a regra na skill; não autoriza gravar esse expediente no SPA.

## Agravo interno — julgamento monocrático de mérito desfavorável ao Estado

Aplicar em processos de competência de Fora do SUS ou Internação Psiquiátrica quando o PDF comunicar julgamento monocrático de mérito desfavorável ao Estado. Considerar o efeito concreto do dispositivo sobre o Estado, independentemente de quem interpôs o recurso:

- Recurso do Estado não provido, com resultado desfavorável ao Estado.
- Recurso do Município ou da parte autora/particular provido, desde que o resultado seja desfavorável ao Estado. Não presumir prejuízo estadual apenas porque o recurso de outra parte foi provido.

Preencher manifestação `Agravo interno` e observação do processo exatamente `[PREFIXO] — Julgamento monocrático de mérito desfavorável ao Estado. Triagem automatizada 🤖.`, substituindo PREFIXO por FSUS ou IP conforme a caixa. Como regra, não criar tarefa de Ofício e deixar os parâmetros de tarefa vazios, ressalvada a exceção de nova tutela concedida ao particular abaixo. Esta regra específica prevalece sobre orientações anteriores conflitantes de Ofício para esse fluxo.

Deixar Assessor em branco em Agravo interno; a designação será definida futuramente.

Não aplicar automaticamente esta regra à simples negativa de efeito suspensivo ou ao não conhecimento do recurso: essas hipóteses permanecem para revisão específica. Para julgamento parcialmente favorável, aplicar a extensão abaixo. Preservar a exceção de julgamento atual de Embargos de Declaração. A aprovação desta regra autoriza sua persistência na skill, não a execução no SPA sem autorização correspondente.

### Exceção de Ofício no agravo interno: tutela concedida em recurso do particular

Criar tarefa de Ofício quando o recurso da parte autora/particular for provido para conceder tutela de urgência anteriormente indeferida em primeiro grau e a decisão de segundo grau impuser cumprimento ao Estado. Confirmar essa sequência no conteúdo dos atos e o comando dirigido ao Estado; não presumir concessão de tutela apenas porque o recurso do particular foi provido. Se o PDF não permitir confirmar a providência, consultar o PJe para obter o contexto faltante.

- Manter Agravo interno e a observação `[PREFIXO] — Julgamento monocrático de mérito desfavorável ao Estado. Triagem automatizada 🤖.`, quando presentes as condições da regra de mérito monocrático acima.
- Comunicar a nova obrigação: CUMP GERAL sem multa pertinente ao Estado; CUMP MULTA quando houver incidência de multa pertinente ao Estado; SECUND quando o cumprimento primário for de outro ente e o Estado tiver responsabilidade secundária. Usar as redações específicas aprovadas para cada modalidade.
- Designar YASMIM MARQUES NASCIMENTO e selecionar o dia seguinte à criação em America/Cuiaba, pulando somente sábados e domingos e sem considerar feriados. Deixar prazo em dias úteis vazio.
- Se o julgamento apenas mantiver obrigação anteriormente imposta ao Estado, não criar Ofício por esta regra.
- Não ampliar esta exceção para recurso do Município sem regra própria aprovada. A última orientação aprovada trata especificamente do recurso do particular.
- A concessão provisória de tutela recursal, isoladamente, não equivale a julgamento monocrático de mérito: não confirmar Agravo interno com base apenas nessa concessão se faltar julgamento de mérito; submeter essa hipótese à revisão específica.

### Extensão: julgamento monocrático de mérito parcialmente favorável

Confirmar Agravo interno quando o julgamento monocrático de mérito for desfavorável ao Estado, total ou parcialmente, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Usar manifestação `Agravo interno` e manter a observação padrão `[PREFIXO] — Julgamento monocrático de mérito desfavorável ao Estado. Triagem automatizada 🤖.` Registrar na análise que o resultado foi parcialmente favorável e quais capítulos desfavoráveis remanescem, sem descrever o resultado como integralmente desfavorável.
- Manter as regras de assessor e de Ofício do fluxo de Agravo interno: não criar Ofício pela mera manutenção de obrigação anterior; aplicar somente a exceção de nova tutela em recurso do particular quando suas condições estiverem confirmadas.
- Verificar competência antes de aplicar a classificação. Se o usuário determinar redistribuição/reclassificação interna ou o objeto pertencer a outro subsetor, separar para esse fluxo, cuja regra ainda será definida, sem classificar automaticamente como Agravo interno neste subsetor.
- Os processos 1018364-43.2021.8.11.0015 e 1027612-05.2026.8.11.0000 foram expressamente separados pelo usuário para redistribuição/reclassificação interna. São exemplos de manutenção de capítulos desfavoráveis em resultado parcialmente favorável, mas não estão autorizados para execução de Agravo interno no SPA nesta etapa.

## Encerramento sem Ofício — duplicidade / preclusão consumativa

Sugerir encerramento, sem criar tarefa de Ofício, quando o recurso não for conhecido por duplicidade/preclusão consumativa e a consulta aos autos pelo MCP PJe CDSP confirmar que o Estado efetivamente interpôs dois recursos contra a mesma decisão, com repetição da impugnação.

Antes de aplicar:

1. Consultar obrigatoriamente os autos pelo MCP PJe CDSP; a fundamentação do PDF do SPA, sozinha, não basta para confirmar a duplicidade.
2. Identificar os números dos dois recursos e conferir suas petições e a decisão impugnada em cada um.
3. Confirmar que ambos foram interpostos pelo Estado contra a mesma decisão e repetem a impugnação, caracterizando a preclusão consumativa. Não confundir recursos contra decisões diferentes com duplicidade; resolver divergências sobre a identidade do recorrente antes de concluir.
4. Registrar na análise os números dos recursos, documentos e decisão que sustentam a confirmação. Se a consulta for insuficiente ou não confirmar a duplicidade, manter revisão necessária, sem executar encerramento por esta regra.

Observação proposta: `[PREFIXO] — Recurso não conhecido por duplicidade. Preclusão consumativa confirmada no PJe. Triagem automatizada 🤖.`, substituindo PREFIXO por FSUS ou IP conforme a caixa. Não inventar campo de observação em formulário que não o disponibilize; manter a fundamentação no relatório quando necessário.

Encerrar somente o expediente referente ao recurso duplicado, preservando o acompanhamento do primeiro recurso e das obrigações na origem. Não criar tarefa de Ofício e não classificar automaticamente como Agravo interno nessa hipótese confirmada. Usar o fluxo de sugestão de encerramento, com Outros e encaminhamento vigente conforme as regras operacionais, sem confundir sugestão com encerramento definitivo.

Os processos 1045959-86.2026.8.11.0000 e 1045957-19.2026.8.11.0000 são candidatos a esta regra; a leitura anterior do relatório não substitui a conferência exigida acima. A aprovação atual salva a regra e não autoriza executar esses expedientes no SPA.

## Contrarrazões — FSUS e Internação Psiquiátrica

Aplicar somente quando o objeto for de competência de Fora do SUS ou Internação Psiquiátrica. Casos de outros subsetores ficam para redistribuição/reclassificação interna, sem aplicar automaticamente este preenchimento.

1. Ler primeiro a intimação no SPA. Se ela determinar genericamente apresentar contrarrazões, sem identificar o recurso, consultar obrigatoriamente os autos pelo MCP PJe CDSP para identificá-lo.
2. Identificar a modalidade do recurso, o recorrente, o ID da petição recursal e a pretensão recursal. Complementar pelo MCP PJe quaisquer dessas informações ausentes. Ler a petição quando necessário para resumir fielmente o pedido, sem confundir pedido recursal com decisão já proferida.
3. Confirmar exatamente `Contrarrazões` no campo de manifestação, independentemente da via recursal e de o recorrente ser Município, União, Ministério Público ou parte autora/particular. Não selecionar modalidades específicas como Contrarrazões à Apelação nesse campo. Inspecionar as opções atuais; se houver códigos duplicados sem código aprovado para esse fluxo, resolver a opção antes de gravar, sem escolher pela posição.
4. Preencher a observação destinada ao assessor (observação do processo) com recurso, recorrente, ID e pretensão recursal resumida, neste padrão: `[PREFIXO] - Contrarrazões à apelação do Município (id. ID_DO_RECURSO): pretende transferir ao Estado a responsabilidade pelo fornecimento da fórmula. Triagem automatizada 🤖.` Usar FSUS ou IP conforme a caixa e adaptar a regência à modalidade (por exemplo, ao agravo interno, ao agravo de instrumento ou ao recurso inominado). O texto da pretensão é individualizado; não copiar o exemplo como pedido de todos os casos.
5. Não criar tarefa de Ofício em Contrarrazões, qualquer que seja a via recursal. Deixar todos os parâmetros/campos de tarefa vazios, inclusive tipo, destinatário, vencimento e observação de Ofício. Esta regra específica prevalece sobre sugestões anteriores de Ofício neste fluxo.
6. Não aplicar a dispensa/encerramento por honorários inferiores a R$ 5 mil quando o recurso pretender transferir ou aumentar esse encargo ao Estado. Confirmar Contrarrazões também nesses casos, observada a competência FSUS/IP.
7. Se a consulta não esclarecer o recurso ou os dados necessários à observação, sinalizar a pendência; não inventar informações nem gravar marcadores como “id. a conferir”.
8. Deixar Assessor em branco em Contrarrazões, independentemente do recurso ou recorrente.

Salvar esta regra não autoriza por si só executar os casos do relatório no SPA. Preservar a exceção geral quando o ato atual julgar Embargos de Declaração; distinguir esse julgamento de intimação para responder a recurso.

### Código padrão de Contrarrazões

Por autorização do usuário para definir uma opção padrão, adotar `OPT040212` — `Contrarrazões` no fluxo FSUS. A opção homônima `OPT037950` não é o padrão deste fluxo. Código validado nos seis registros executados em 15/10/2026. Conferir se o código e o texto continuam presentes no formulário; para IP, inspecionar antes de aplicar, sem presumir transporte de códigos entre fluxos.

## Apelação e Recurso Inominado — regra conjunta

Confirmar Apelação ou Recurso Inominado quando a sentença de mérito for desfavorável ao Estado, total ou parcialmente, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica, observadas as exceções já aprovadas.

- Selecionar manifestação `Apelação` ou `Recurso inominado` conforme o rito confirmado nos autos. Não confundir sentença recorrível por Recurso Inominado com sentença recorrível por Apelação; não decidir o rito apenas pela existência de condenação.
- Preencher observação do processo exatamente `[PREFIXO] — Sentença de mérito desfavorável ao Estado. Triagem automatizada 🤖.`, usando FSUS ou IP conforme a caixa.
- Não criar tarefa de Ofício em Apelação ou Recurso Inominado, inclusive se a sentença conceder tutela anteriormente indeferida. Deixar todos os campos/parâmetros de tarefa vazios: tipo, destinatário, prazo, vencimento e observação de Ofício. Esta orientação específica prevalece sobre sugestões anteriores de Ofício nesses fluxos; não transportar a exceção de Ofício do Agravo interno para Apelação ou Recurso Inominado.
- Preservar as exceções aprovadas sobre julgamento exclusivamente de honorários e direcionamento primário municipal; não revogá-las pela regra geral. Preservar também a exceção do ato atual que julga Embargos de Declaração.
- Deixar Assessor em branco em Apelação e Recurso Inominado.
- Inspecionar as opções atuais e usar códigos aprovados para o fluxo, sem escolher pela posição entre opções homônimas. A aprovação desta regra não autoriza por si só executar os casos no SPA.

### Códigos aprovados de Apelação e Recurso Inominado

No fluxo FSUS, usar `OPT036330` — `Apelação` e `OPT030399` — `Recurso inominado`, aprovados pelo usuário e validados na execução dos oito casos em 15/10/2026. Não usar as opções homônimas `OPT037919` e `OPT037945` como padrão. Conferir a presença do código/texto no formulário atual. Para IP, inspecionar e validar o fluxo antes de transportar códigos.

### Restituição ao Estado na sentença e orientação adicional sobre dados bancários

Quando a sentença determinar restituição ou ressarcimento de valores ao Estado, não adotar providência adicional relativa à restituição se não houver ordem ou intimação dirigida ao Estado/PGE para informar dados bancários. Não interpretar a simples determinação de devolver valores ao Estado como dever da PGE de promover a transferência ou comprovar o recolhimento.

Se houver ordem ou intimação ao Estado/PGE para informar dados bancários para restituição, manter a manifestação principal cabível, como Apelação ou Recurso inominado, e acrescentar à observação destinada ao assessor a orientação extra: `Informar dados bancários para restituição ao Estado.` Manter Assessor em branco. Não substituir a manifestação principal por Manifestação nem criar Ofício apenas por essa orientação adicional.

Esta regra específica prevalece sobre o fluxo genérico de dados bancários quando a restituição vier na sentença juntamente com outra manifestação principal. Aplicar em matéria FSUS/IP. No expediente 54144272, processo 1020930-28.2026.8.11.0002, tratar o saldo de R$ 1,91 como restituição ao Estado: ausente ordem para o Estado/PGE informar dados bancários, não acrescentar providência pela restituição e manter Apelação pela obrigação de fornecimento. Esta definição não implica gravação do expediente no SPA.

## Impugnação ao cumprimento de sentença — FSUS e IP

Confirmar Impugnação ao cumprimento de sentença quando se tratar de execução de obrigação de fazer relacionada à saúde, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica. Não aplicar automaticamente à execução exclusiva de honorários ou de obrigação de pagar.

Aplicar integralmente esta mesma regra ao cumprimento provisório de decisão interlocutória que execute obrigação de fazer relacionada à saúde, inclusive quando houver ordem para comprovar o cumprimento em 24 horas, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica. Manter a manifestação `Impugnação ao cumprimento de sentença`, a observação individualizada, Assessor em branco e as mesmas regras de Ofício abaixo. Não exigir sentença como condição para este enquadramento. Distinguir a execução da decisão da mera intimação da tutela na fase de conhecimento.

- Selecionar manifestação `Impugnação ao cumprimento de sentença`. Inspecionar o formulário e usar o código aprovado para o fluxo, sem escolher pela posição entre opções homônimas.
- Preencher observação destinada ao assessor (observação do processo): `[PREFIXO] - Execução de obrigação de fazer para [descrever brevemente a obrigação de saúde]. Triagem automatizada 🤖.` Substituir PREFIXO por FSUS ou IP conforme a caixa e individualizar a obrigação efetivamente executada. Não repetir o nome da manifestação nessa observação.
- Deixar Assessor em branco em Impugnação ao cumprimento de sentença, em FSUS e IP.
- Criar tarefa de Ofício segundo as mesmas regras da Contestação:
  - Sem multa pertinente ao Estado e sem responsabilidade secundária: `Enviar ofício "CUMP GERAL" - Cumprimento de decisão judicial.`
  - Com multa pertinente ao Estado: `Enviar ofício "CUMP MULTA" - Cumprimento de decisão judicial c/ incidência de multa.`
  - Responsabilidade secundária do Estado: `Enviar ofício "SECUND" - Responsabilidade secundária ao Estado.`
- Usar tipo Ofício, destinatária YASMIM MARQUES NASCIMENTO e vencimento no dia seguinte à criação em America/Cuiaba, pulando apenas sábados e domingos, sem considerar feriados. Deixar prazo em dias úteis vazio. Manter observação da tarefa separada da observação do processo.
- Esta regra específica prevalece sobre orientações anteriores conflitantes sobre confirmação da manifestação e criação de Ofício neste fluxo. Preservar a exceção geral quando o ato atual julgar Embargos de Declaração.
- A aprovação desta regra autoriza sua persistência na skill; não autoriza por si só executar expedientes no SPA.

### Código padrão de Impugnação ao cumprimento de sentença

Por autorização expressa do usuário para escolher e definir uma opção, adotar `OPT040771` — `Impugnação ao cumprimento de sentença` como padrão em FSUS e IP. A opção `OPT037930` — `Impugnação ao Cumprimento de Sentença` não é o padrão desses fluxos.

Conferir a presença do código e do texto no formulário do expediente exato antes de gravar, em cada caixa. A opção OPT040771 foi apresentada nas inspeções FSUS e IP desta conversa; a definição do padrão não equivale a teste de salvamento no IP. Se o código não estiver disponível ou o texto divergir, sinalizar a pendência em vez de substituir automaticamente pela opção homônima. Manter Assessor em branco e as demais regras de observação e Ofício acima. Esta definição não implica, por si só, gravação dos expedientes pendentes no SPA.

## Manifestação sobre laudo pericial — FSUS e IP

Confirmar `Manifestação` quando houver intimação expressa para manifestar-se sobre laudo pericial, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Manter Assessor em branco.
- Preencher a observação do processo exatamente no padrão `[PREFIXO] - Manifestar-se sobre o laudo pericial id. [ID DO LAUDO]. Triagem automatizada 🤖.`, substituindo PREFIXO por FSUS ou IP e o marcador pelo ID efetivo do laudo. Identificar apenas o ID do laudo, sem descrever o objeto da perícia nessa observação.
- Não criar tarefa de Ofício; deixar todos os campos/parâmetros de tarefa vazios.
- Se a intimação não permitir confirmar a competência ou o ID do laudo, consultar o MCP PJe para esclarecer. Se a informação continuar ausente, manter pendente e relatar o impedimento, sem inventar o ID.
- Inspecionar as opções atuais do campo Manifestação. Adotar o padrão `OPT040586` — `Manifestação`, conferindo código e texto no formulário e validando separadamente o fluxo IP antes de aplicar. Não selecionar as opções homônimas pela posição.
- Distinguir esta hipótese das intimações para apresentar quesitos ou especificar provas, que têm regras próprias.

## Alegações finais — FSUS e Internação Psiquiátrica

Confirmar Alegações finais quando houver intimação expressa para apresentação de alegações finais, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Selecionar manifestação `Alegações finais`, conferindo o código e o texto no formulário atual e resolvendo opções homônimas antes de gravar.
- Preencher observação destinada ao assessor (observação do processo): `[PREFIXO] - Apresentar alegações finais: [identificar a pretensão]. Triagem automatizada 🤖`.
- Substituir PREFIXO por FSUS ou IP conforme a caixa e descrever de forma sucinta a pretensão concreta, sem gravar os marcadores do modelo. Exemplo: `FSUS - Apresentar alegações finais: imunoterapia para alergias. Triagem automatizada 🤖`.
- Deixar o campo Assessor em branco.
- Não criar tarefa de Ofício. Deixar todos os campos/parâmetros de tarefa vazios: tipo, destinatário, prazo, vencimento e observação de Ofício.
- Não inferir esta manifestação apenas pela fase do processo: exigir o comando expresso da intimação e confirmar a competência do subsetor. Sinalizar insuficiência documental em vez de inventar dados.
- A aprovação desta regra autoriza sua persistência na skill, não a execução no SPA sem autorização correspondente.

### Código aprovado de Alegações finais

No fluxo FSUS, usar `OPT027234` — `Alegações finais`, aprovado pelo usuário e validado no expediente 54025000 em 15/10/2026. Não usar a opção homônima `OPT037918` como padrão. Conferir código/texto no formulário atual; validar separadamente antes de transportar o código para IP.

## Petição de quesitos — FSUS e Internação Psiquiátrica

Confirmar Petição de quesitos quando houver intimação expressa para apresentar quesitos e/ou indicar assistente técnico, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Selecionar manifestação `Petição de quesitos`, conferindo código e texto no formulário atual.
- Preencher observação destinada ao assessor: `[PREFIXO] - Apresentar quesitos e avaliar indicação de assistente técnico: [identificar a pretensão]. Triagem automatizada 🤖`. Usar FSUS ou IP conforme a caixa e descrever a pretensão efetiva; adaptar as providências ao comando expresso, sem acrescentar etapa não determinada.
- Deixar Assessor em branco.
- Não criar Ofício; deixar todos os campos/parâmetros de tarefa vazios.
- Não inferir a manifestação apenas pela existência de perícia. Exigir intimação expressa e competência FSUS/IP; sinalizar insuficiência documental.
- Exemplo validado: `FSUS - Apresentar quesitos e avaliar indicação de assistente técnico: fornecimento de Nutrimais Kids e Alfamino. Triagem automatizada 🤖`.

## Produção de provas — FSUS e Internação Psiquiátrica

Confirmar Produção de provas quando houver intimação expressa para especificar provas, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Selecionar manifestação `Produção de provas`, conferindo código e texto no formulário atual.
- Preencher observação destinada ao assessor: `[PREFIXO] - Especificar provas, justificando sua pertinência: [identificar a pretensão]. Triagem automatizada 🤖`. Usar FSUS ou IP conforme a caixa e individualizar a pretensão concreta, sem gravar marcadores do modelo.
- Deixar Assessor em branco.
- Não criar Ofício; deixar todos os campos/parâmetros de tarefa vazios.
- Exigir comando expresso da intimação e confirmar competência FSUS/IP; não inferir a manifestação apenas pela fase processual. Sinalizar insuficiência documental.

## Regras de encerramento — FSUS e Internação Psiquiátrica

Aplicar somente a expedientes de competência de Fora do SUS ou Internação Psiquiátrica. Registrar sugestão de encerramento no SPA, distinguindo-a de encerramento definitivo. Esta seção reúne as três hipóteses aprovadas abaixo; demais hipóteses dos materiais de referência permanecem pendentes de revisão individual, sem execução automática até validação do usuário.

### 1. Intimação de pauta de julgamento

Aplicar à intimação de pauta de julgamento de recurso no TJMT ou TRF-1, incluindo Turmas Recursais. Observação exata: `Intimação de pauta de julgamento de recursos em trâmite no TJMT ou TRF-1, cujo futuro acórdão será posteriormente objeto de nova intimação da PGE.`

Não criar Ofício nem tarefa de cadastramento de pauta. Esta orientação substitui a proposta anterior de cadastrar pautas de Turmas Recursais. Preservar a redação exata, sem acrescentar prefixo ou assinatura automatizada a essa observação específica.

### 2. Recurso duplicado — preclusão consumativa

Aplicar ao recurso não conhecido por duplicidade/preclusão consumativa quando consulta obrigatória pelo MCP PJe confirmar efetivamente dois recursos do Estado contra a mesma decisão com repetição da impugnação. Conferir petições, recorrente e decisão impugnada conforme detalhado na regra específica anterior. Se não confirmar, sinalizar revisão necessária.

Observação: `[PREFIXO] — Recurso não conhecido por duplicidade. Preclusão consumativa confirmada no PJe. Triagem automatizada 🤖.`, com FSUS ou IP. Não criar Ofício. Encerrar somente o expediente do recurso duplicado, preservando o primeiro recurso e as obrigações na origem.

### 3. Julgamento sobre honorários, inclusive com custas municipais

Sugerir encerramento da intimação, sem ofício, quando o julgamento tratar exclusivamente de honorários e o encargo atribuído ao Estado não superar R$ 5.000,00, inclusive após rateio de 50%, ou quando os honorários forem atribuídos exclusivamente ao Município ou à União, sem encargo para o Estado, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Abranger também o julgamento que decida custas municipais e honorários, sem modificar a obrigação de saúde, observadas as mesmas condições de competência e de encargo estadual acima. A apreciação de custas municipais no mesmo ato não impede o encerramento sem Ofício por esta regra. O expediente 67355062, processo 1041677-13.2025.8.11.0041, exemplifica a extensão: isenção de custas municipais e honorários totais de R$ 3.000,00 rateados igualmente, cabendo R$ 1.500,00 ao Estado, sem alteração do fornecimento.

### Execução e limitações

Usar motivo Outros e preservar encaminhamento vigente, conforme contrato operacional do MCP. Conferir o formulário antes de gravar. Quando a hipótese exigir observação exata, usar fluxo que permita registrá-la; não afirmar que a observação foi salva se a ferramenta não aceitar esse campo. Não executar parcialmente um pedido que exija essa observação sem informar a limitação e resolver o meio de registro. Manter campos de tarefa vazios para essas três hipóteses.

### 4. Negativa de efeito suspensivo — regra de encerramento atual

Sugerir encerramento da intimação, sem Ofício, quando a decisão monocrática negar efeito suspensivo a agravo de instrumento interposto pelo Estado de Mato Grosso, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Observação exata: `[PREFIXO] - Decisão monocrática denegatória de efeito suspensivo. Decisão contra qual não se recorre. Triagem automatizada 🤖.` Usar FSUS ou IP conforme a caixa. Tratar “Decisão contra qual não se recorre” como orientação interna de triagem do usuário para esse fluxo, não como afirmação universal de irrecorribilidade legal.

Não criar Ofício; deixar todos os campos de tarefa vazios. O encerramento limita-se à intimação e preserva o acompanhamento do mérito do agravo.

Por orientação expressa atual, não exigir leitura das razões para pesquisar impugnação de multa cominatória como condição deste encerramento e não confirmar Agravo interno por essa exceção anterior. Esta regra substitui os critérios anteriores conflitantes da matriz Gemini e da skill para a negativa de efeito suspensivo. Não confundir com julgamento de mérito do agravo.

Esta é a quarta hipótese aprovada da seção Regras de encerramento. Preservar as limitações operacionais quanto ao registro da observação exata no SPA. Salvar a regra não autoriza por si só executar expedientes no SPA.

### 5. Extinção, arquivamento ou suspensão provisória

Sugerir encerramento da intimação, sem ofício, quando o ato judicial determinar a extinção ou o arquivamento do processo ou do cumprimento de sentença por perda do interesse processual, desistência ou satisfação da obrigação (art. 924, II, do CPC), ou determinar sua suspensão provisória, inclusive com arquivamento provisório durante o período de suspensão, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

### 6. Extinção por óbito da parte autora

Sugerir encerramento da intimação, sem ofício, quando o ato judicial determinar a extinção do processo por óbito da parte autora, desde que o Estado não tenha sido condenado ao pagamento de honorários superiores a R$ 5.000,00 e o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

### 7. Intimação meramente informativa sobre pagamento ou alvará

Sugerir encerramento da intimação, sem ofício, quando se tratar de mera comunicação sobre pagamento ou alvará, sem ordem ao Estado/PGE para devolução de saldo residual, prestação de contas, resposta ou outra providência, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

## Manifestação — dados bancários para devolução de saldo residual

Confirmar Manifestação quando houver determinação expressa para o Estado/PGE informar dados bancários ou intimação genérica para devolução de saldo residual, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

- Manifestação: `Manifestação`. Conferir o código e o texto no formulário atual; não selecionar entre opções homônimas pela posição.
- Assessor: em branco.
- Observação ao assessor (observação do processo): `[FSUS ou IP] Informar dados bancários para devolução de saldo residual. Triagem automatizada`
- Substituir `[FSUS ou IP]` pelo prefixo correspondente à caixa, sem colchetes. Preservar a redação específica aprovada, sem acrescentar hífen ou emoji automaticamente.
- Ofício: não criar; deixar todos os campos/parâmetros de tarefa vazios.

Distinguir esta hipótese da comunicação de devolução já realizada sem providência ao Estado: nessa última, aplicar a regra de encerramento informativo. Não encerrar como mera comunicação quando houver a determinação expressa ou a intimação genérica para devolução de saldo residual descritas acima.

### Código aprovado de Manifestação para dados bancários

No fluxo FSUS de dados bancários para devolução de saldo residual, usar `OPT040586` — `Manifestação`, aprovado pelo usuário e validado nos expedientes 54014053, 54012980 e 54025729. As opções homônimas `OPT037960` e `OPT040585` não são o padrão deste fluxo. Conferir código/texto no formulário atual e validar separadamente antes de transportar para IP.

### 8. Comando dirigido exclusivamente a outra parte ou ente

Sugerir encerramento da intimação, sem ofício, quando o comando judicial for dirigido exclusivamente à parte autora, Ministério Público, Defensoria Pública, Município, União ou terceiro interessado, sem ordem ao Estado/PGE para resposta ou outra providência, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Aplicar a hipótese de terceiro interessado independentemente da obrigação ou ordem que o juiz lhe imponha, inclusive quando o destinatário for clínica, hospital, farmácia ou outro prestador de serviços de saúde afins. Abranger, por exemplo, constituição de novo advogado, informações sobre evolução do tratamento e previsão de alta. O critério é a ausência de ordem ao Estado/PGE para resposta ou outra providência, e não o conteúdo da obrigação imposta ao terceiro. Ler o ato integralmente para conferir essa ausência e a competência FSUS/IP; não criar tarefa de Ofício.

### 9. Mero retorno ou remessa dos autos

Sugerir encerramento da intimação, sem ofício, quando se tratar de intimação meramente informativa de retorno ou remessa dos autos, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Abranger também a comunicação de retorno ou remessa acompanhada de abertura de prazo genérico para as partes “requererem o que entenderem de direito” ou expressão equivalente, inclusive sob pena de arquivamento. Essa abertura genérica de prazo não impede a sugestão de encerramento da intimação, sem Ofício, quando não houver comando específico ao Estado/PGE para resposta, cumprimento ou outra providência.

Ler o ato integralmente para distinguir a faculdade genérica de requerer de uma determinação específica. Havendo comando específico ao Estado/PGE, analisar a regra própria, sem encerrar automaticamente pela regra 9. Limitar a sugestão à intimação, preservando o acompanhamento dos autos e das obrigações anteriores. O expediente 54192252, processo 1000690-61.2025.8.11.0096, exemplifica a extensão aprovada: retorno da instância superior com dez dias para requerer o que entender de direito, sob pena de arquivamento. A inclusão desta regra não implica, por si só, gravação desse expediente no SPA.

### 10. Comunicação de decisão recursal nos autos de origem

Sugerir encerramento da intimação, sem ofício, quando se tratar de mera comunicação, nos autos de origem, de decisão proferida em recurso, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica, preservando a análise e a atuação no expediente recursal próprio.

### 11. Recurso prejudicado por sentença superveniente

Sugerir encerramento da intimação, sem ofício, quando o recurso do Estado, Município, União ou da parte autora for julgado prejudicado por sentença superveniente, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

### 12. Agravo ou apelação exclusivamente de outro ente ou particular não conhecido ou desprovido

Sugerir encerramento da intimação, sem criar tarefa de Ofício, quando decisão monocrática ou acórdão não conhecer ou negar provimento a recurso de agravo ou apelação interposto exclusivamente pelo Município, União ou particular, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica. Abranger agravo de instrumento e agravo interno; conferir a modalidade e o recorrente no ato integral.

- Confirmar que o recurso julgado é exclusivamente do Município, União ou particular; não presumir o recorrente pela posição no cabeçalho ou pela presença do Estado como agravado/apelado.
- Não exigir que a obrigação anterior seja exclusivamente municipal: a manutenção de obrigação estadual anterior não afasta esta hipótese. Preservar o acompanhamento dessa obrigação na origem.
- Não estender automaticamente a provimento parcial, conhecimento parcial, recurso do Estado ou julgamento conjunto que também decida recurso estadual; analisar separadamente os capítulos e sinalizar o que não estiver coberto por regra aprovada.
- Preservar a exceção prioritária quando o ato atual julgar Embargos de Declaração. Não incluir Ministério Público ou Defensoria Pública como recorrentes autônomos por analogia a particular; distinguir a parte particular representada pela Defensoria.
- Usar sugestão de encerramento com motivo Outros e encaminhamento vigente, conforme o contrato operacional. Não criar Ofício nem preencher campos de tarefa. Limitar a sugestão à intimação, sem afirmar encerramento definitivo do processo.

A aprovação desta regra autoriza sua persistência na skill; não implica, por si só, gravação de expedientes anteriores no SPA.

### 13. Não conhecimento do recurso com declinação de competência

Sugerir encerramento da intimação, sem criação de tarefa de Ofício, quando o julgamento não conhecer do recurso por incompetência do órgão julgador e declinar da competência, determinando a remessa ao órgão competente, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica. Abranger remessa à Turma Recursal ou à Justiça Federal quando esse for o resultado concreto do ato.

Conferir o fundamento e o dispositivo completos; distinguir não conhecimento por incompetência de outras causas de inadmissibilidade. Abranger a redação equivalente que reconhece a incompetência, determina a remessa e declara prejudicada a análise do recurso por esse fundamento, como no expediente 67388043, processo 1047439-02.2026.8.11.0000. Usar motivo Outros e preservar o encaminhamento vigente no SPA, sem preencher campos de tarefa. Preservar a exceção prioritária dos julgamentos de Embargos de Declaração. Não generalizar esta hipótese para qualquer não conhecimento ou prejudicialidade de recurso.

### 14. Aquisição determinada em conciliação ou mediação assíncrona

Sugerir encerramento da intimação, sem criação de tarefa de Ofício, quando a decisão, no âmbito de conciliação ou mediação assíncrona, determinar a aquisição de medicamento, produto ou insumo por fornecedor indicado, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Aplicar também quando a decisão estabelecer entrega à Secretaria de Saúde, SAF ou unidade equivalente, posterior disponibilização ao paciente, prestação de contas e liberação de pagamento ao fornecedor.

A determinação à Secretaria de Saúde para cumprir a decisão e informar ao juízo as providências adotadas não impede o encerramento sem Ofício nesta hipótese. Esta regra específica prevalece sobre a restrição de encerramento por existência desses comandos ao ente estadual.

Conferir o ato integralmente e a competência do subsetor. Usar motivo Outros, preservar o encaminhamento vigente no SPA e deixar todos os campos de tarefa vazios. Preservar a exceção prioritária dos julgamentos de Embargos de Declaração.

### 18. Comunicação de penhora ou bloqueio já realizado

Sugerir encerramento da intimação, sem criação de tarefa de Ofício, quando o ato comunicar penhora ou bloqueio de valores já realizado, inclusive com abertura de prazo para as partes se manifestarem, querendo, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Aplicar quando a intimação se limitar à ciência da constrição e à oportunidade de manifestação, sem determinar nova providência de fornecimento, pagamento, prestação de contas ou cumprimento ao Estado/PGE.

Usar motivo Outros, preservar o encaminhamento vigente no SPA e deixar todos os campos de tarefa vazios.

## Encerramento com criação de Ofício

### 15. Intimação na origem para cumprimento de tutela recursal

Sugerir encerramento da intimação, com criação de tarefa de Ofício, quando o juízo de origem intimar o Estado/PGE para cumprir tutela de urgência concedida em recurso da parte autora contra o indeferimento da liminar, antes ou após a apresentação da contestação, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Ler integralmente o ato da origem e a decisão recursal para identificar a obrigação, o responsável primário, o prazo de cumprimento e eventual multa. Criar o Ofício conforme o comando concreto:

| Situação | Observação da tarefa |
|---|---|
| Cumprimento primário pelo Estado, sem multa pertinente | `Enviar ofício "CUMP GERAL" - Cumprimento de decisão judicial.` |
| Cumprimento estadual com incidência de multa | `Enviar ofício "CUMP MULTA" - Cumprimento de decisão judicial c/ incidência de multa.` |
| Cumprimento primário por outro ente e responsabilidade secundária do Estado | `Enviar ofício "SECUND" - Responsabilidade secundária ao Estado.` |

A mera previsão de bloqueio de valores não equivale à incidência de multa.

Designar a tarefa a YASMIM MARQUES NASCIMENTO, com vencimento no próximo dia de segunda a sexta posterior à criação, em America/Cuiaba, pulando apenas sábados e domingos. Deixar o prazo em dias úteis em branco.

Registrar a sugestão de encerramento com motivo Outros, preservando o encaminhamento vigente. Confirmar a criação do Ofício antes de encaminhar o encerramento. Se a integração não permitir executar ambas as providências preservando a identidade do expediente, informar a limitação e não registrar encerramento isolado.

### 16. Manifestação sobre prestação de contas, notas fiscais e comprovantes de fornecimento

Sugerir encerramento da intimação, com criação de tarefa de Ofício, quando o Estado/PGE for intimado a manifestar-se sobre prestação de contas, notas fiscais, declarações ou comprovantes de fornecimento, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Aplicar também quando a manifestação for determinada após a expedição de alvará ou liberação de pagamento ao fornecedor.

Criar tarefa do tipo Ofício, com a observação exatamente: `Enviar ofício "PREST" - Prestação de Contas.`

Designar a tarefa a YASMIM MARQUES NASCIMENTO, com vencimento no próximo dia de segunda a sexta posterior à criação, em America/Cuiaba, pulando apenas sábados e domingos. Deixar o prazo em dias úteis em branco.

Registrar a sugestão de encerramento com motivo Outros, preservando o encaminhamento vigente. Confirmar a criação do Ofício antes de encaminhar o encerramento. Se a integração não permitir executar ambas as providências preservando a identidade do expediente, informar a limitação e não registrar encerramento isolado.

Essa hipótese abrange os expedientes 54007275 e 54127060.

### 17. Ordem de cumprimento, fornecimento, entrega ou justificativa

Aplicar quando a intimação determinar ao Estado o cumprimento de liminar, o fornecimento ou a entrega de produto, insumo ou tratamento, ou a apresentação de justificativa para o não atendimento, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

**1. Existência de liminar identificável pelo conteúdo da intimação**

Sugerir encerramento da intimação, com criação de tarefa de Ofício, quando o conteúdo permitir identificar a existência de liminar que imponha obrigação ao Estado.

**2. Existência de liminar não identificável pelo conteúdo da intimação**

Confirmar a manifestação Agravo de instrumento, mantendo o campo Assessor em branco, e preencher a observação:

`[FSUS ou IP] - Verificar a existência de decisão que imponha obrigação ao Estado e avaliar o cabimento de agravo de instrumento. Triagem automatizada 🤖.`

**Tarefa de Ofício — obrigatória nas duas hipóteses**

Criar a tarefa durante a triagem, conforme o comando identificado:

| Situação | Observação da tarefa |
|---|---|
| Cumprimento estadual sem multa pertinente e sem responsabilidade secundária | `Enviar ofício "CUMP GERAL" - Cumprimento de decisão judicial.` |
| Cumprimento estadual com incidência de multa | `Enviar ofício "CUMP MULTA" - Cumprimento de decisão judicial c/ incidência de multa.` |
| Cumprimento primário de outro ente e responsabilidade secundária do Estado | `Enviar ofício "SECUND" - Responsabilidade secundária ao Estado.` |

A mera previsão de bloqueio de valores não equivale à incidência de multa. Não presumir multa ou responsabilidade secundária ausentes do documento.

Designar o Ofício a YASMIM MARQUES NASCIMENTO, com vencimento no próximo dia de segunda a sexta posterior à criação, em America/Cuiaba, pulando apenas sábados e domingos. Deixar o prazo em dias úteis em branco.

Inspecionar o formulário e conferir o código e o texto da manifestação antes de gravar. Não selecionar automaticamente entre opções duplicadas sem código padrão aprovado.

Na hipótese de encerramento, usar motivo Outros, preservar o encaminhamento vigente e confirmar a criação do Ofício antes de encaminhar. Se a integração não permitir executar as duas providências preservando a identidade do expediente, informar a limitação e não registrar encerramento isolado.

## Encerramento mediante confirmação do usuário

As hipóteses desta seção exigem confirmação expressa do usuário antes de registrar a sugestão de encerramento no SPA. A autorização geral para realizar a triagem da caixa não substitui essa confirmação.

Antes de solicitar a confirmação, analisar integralmente o expediente e apresentar: processo, expediente, síntese do julgamento, fundamento para o encerramento e indicação de criação ou dispensa de tarefa de Ofício. Quando houver Ofício proposto, informar sua finalidade, observação, destinatário e vencimento.

Após a confirmação, executar somente as providências autorizadas e conferir o resultado no SPA. Sem confirmação, manter o expediente pendente, sem registrar a sugestão de encerramento nem criar a tarefa vinculada.

### Acórdão que desprove recurso do Estado

Submeter à confirmação do usuário a sugestão de encerramento da intimação de acórdão que negue provimento a recurso interposto pelo Estado de Mato Grosso, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

A sugestão poderá ser acompanhada ou não de tarefa de Ofício, conforme os comandos do julgamento e a confirmação do usuário. Não presumir criação ou dispensa de Ofício apenas pelo desprovimento do recurso.

Preservar a exceção prioritária dos julgamentos de Embargos de Declaração. Não estender automaticamente esta hipótese ao não conhecimento integral ou ao provimento parcial do recurso; o conhecimento parcial com desprovimento da parte conhecida é tratado na hipótese específica abaixo.

### Recurso estadual parcialmente conhecido e desprovido na parte conhecida

Submeter à confirmação expressa do usuário a sugestão de encerramento da intimação de acórdão que conheça parcialmente de recurso interposto pelo Estado de Mato Grosso e negue provimento à parte conhecida, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Identificar quais capítulos não foram conhecidos e os respectivos motivos, quais foram examinados e desprovidos e o efeito concreto sobre a obrigação estadual. Não descrever conhecimento parcial como provimento parcial ou vitória parcial do Estado. Apresentar ao usuário a criação ou dispensa proposta de tarefa de Ofício e, se houver tarefa proposta, sua modalidade, observação, destinatária e vencimento conforme as regras comuns. Aguardar confirmação para as providências propostas, respeitando as limitações do MCP para eventual fluxo combinado.

Preservar a exceção prioritária dos julgamentos de Embargos de Declaração. Não ampliar automaticamente esta hipótese para não conhecimento integral ou provimento parcial do recurso estadual. O expediente 67379554, processo 1030061-33.2026.8.11.0000, exemplifica a hipótese aprovada: questões de marca e direcionamento não conhecidas por falta de interesse recursal, demais questões desprovidas, com manutenção integral da tutela e cumprimento inicial municipal. Sua inclusão na skill não equivale a confirmação para gravar esse expediente no SPA.

### Julgamento conjunto: recurso estadual desprovido e recurso municipal parcialmente provido para direcionamento ao Estado

Submeter à confirmação expressa do usuário a sugestão de encerramento da intimação de acórdão que, em julgamento conjunto, negue provimento ao recurso do Estado de Mato Grosso e dê parcial provimento ao recurso do Município para direcionar o cumprimento primário da obrigação ao Estado, mantendo a responsabilidade do Município em caso de descumprimento estadual. Aplicar somente quando o objeto for de competência de Fora do SUS ou Internação Psiquiátrica.

Identificar separadamente o resultado de cada recurso e a alteração concreta do direcionamento. Apresentar ao usuário a necessidade ou dispensa proposta de Ofício para comunicar o cumprimento primário estadual; não presumir criação ou dispensa. Se proposto Ofício, informar modalidade, observação, destinatária e vencimento conforme as regras comuns e aguardar confirmação antes de criar a tarefa e registrar o encerramento. Respeitar as limitações do MCP para o fluxo combinado, sem gravação parcial não autorizada.

Esta hipótese específica abrange o provimento parcial do recurso municipal descrito acima, sem ampliar automaticamente a regra para provimento parcial de recurso estadual ou outros resultados. Preservar a exceção prioritária dos julgamentos de Embargos de Declaração. O expediente 67355560, processo 1049573-10.2025.8.11.0041, exemplifica a hipótese aprovada. Sua inclusão na skill não equivale a confirmação para gravar esse expediente no SPA.

### Acórdão que cria obrigação para o Estado

Submeter à confirmação expressa do usuário a sugestão de encerramento da intimação de acórdão que crie obrigação para o Estado de Mato Grosso, inclusive ao reformar sentença de improcedência para determinar prestação de saúde, desde que o objeto seja de competência de Fora do SUS ou Internação Psiquiátrica.

Ler o julgamento integralmente e identificar o recorrente, o resultado, a obrigação criada, o destinatário primário, os prazos e eventuais medidas coercitivas. Apresentar ao usuário a proposta de encerramento com ou sem tarefa de Ofício, justificando a necessidade ou dispensa de comunicação da nova obrigação. Se proposto Ofício, informar modalidade, observação, destinatária e vencimento conforme as regras comuns; não presumir criação ou dispensa. Aguardar confirmação expressa antes de registrar o encerramento e criar eventual tarefa vinculada. Respeitar as limitações do MCP para o fluxo combinado, sem gravação parcial não autorizada.

Preservar a exceção prioritária dos julgamentos de Embargos de Declaração. O expediente 67378557, processo 1004834-54.2025.8.11.0007, exemplifica a hipótese aprovada: reforma da improcedência para fornecimento estadual de fórmula infantil. A inclusão desta hipótese na skill não equivale a confirmação para gravar esse expediente no SPA.
