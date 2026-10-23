---
name: fluxo-triagem-minutas
description: Coordena análise dos autos, escolha do modelo no SPA, relatório interno, preenchimento pela skill específica e conferência na mesma minuta usando o MCP Triagem.
---
# Fluxo integrado Triagem e assistente de minutas

## Novo SPA Coreplan — 0.9.5

Para o domínio pge.mt.spa.coreplan.com.br, ler primeiro [percurso e continuidade automática](references/coreplan-095.md) e o [índice de modelos](references/coreplan-modelos.json). Na extensão 0.9.5.2, o percurso autorizado aplica o modelo solicitado mesmo que o formulário sem minuta SPA salva já tenha nome de modelo preexistente; isso é padrão, conforme a referência Coreplan. A IA executa a skill de preenchimento correspondente após identificar e parear a cópia, sem exigir outra ordem por módulo quando o fluxo completo já foi solicitado. A extensão somente navega/seleciona: não executa skills. Os detalhes do SPA antigo abaixo são histórico e não devem ser usados para contornar bloqueios no Coreplan.

## Documentos sem texto e download seletivo

Quando uma leitura dos autos retornar `semTexto`, isso não prova ausência ou ilegibilidade do documento. Se `spa_baixar_documento_autos` estiver disponível e o download estiver abrangido pelo pedido do usuário, usar somente o ID listado no processo atual para obter o PDF necessário, um por vez. O recurso MCP binário fica disponível temporariamente por `resources/read`; verificar que o cliente realmente recebeu o arquivo antes de enviá-lo a OCR/Docling. Não declarar OCR, leitura visual ou análise integral somente porque o download terminou. Ferramenta ou importação indisponível: registrar a limitação e continuar a análise independente. Não baixar todos os autos automaticamente nem deixar de executar o banco integral de preliminares por falha em um comprovante.

## Autorização e sequência

O pedido do usuário para executar este fluxo autoriza análise, relatório interno, preenchimento e conferência segundo as regras expressas da skill do modelo. Não exigir revisão do relatório nem confirmação intermediária de alterações já abrangidas. Preparar as alterações internamente e executá-las pela conexão google_drive/Google Docs do plugin dentro desse escopo, usando controle de revisão quando disponível. Uma proposta interna não autoriza alterações além da skill.

Sequência: ler autos → identificar modelo → confirmar skill específica → selecionar modelo → parear cópia da minuta → relatório interno completo → preenchimento → conferência → resposta final. Substituir minuta já preenchida exige autorização específica, independente do preenchimento modular; não transportar a autorização dada para uma minuta de teste a outra. Não assinar, protocolar nem salvar formulário SPA automaticamente.

## Separação de responsabilidades

O MCP Triagem executa leitura dos autos, navegação, seleção do modelo e identificação da cópia Google Docs associada ao SPA. A conexão google_drive/Google Docs fornecida pelo plugin lê, edita e confere essa cópia. A IA analisa evidências e escolhe o modelo. A skill específica determina campos, condições e limites de alteração. O relatório organiza decisões; não cria teses nem amplia permissões.

O usuário escolheu Triagem + skill específica + conexão Google Drive/Docs do plugin. Manter a exigência de google_drive das skills originais. As funções de escrita direta da Triagem não são a via padrão e não devem ser usadas como alternativa automática se a conexão do plugin falhar. Preservar todas as regras substantivas e de identidade. Não modificar silenciosamente o plugin instalado. Esta skill precisa estar disponível na sessão junto das skills específicas; o arquivo no repositório sozinho não instala um plugin no ChatGPT.

## Modelo e skill aplicável

Não associar modelo a skill por palavra-chave apenas. Confirmar nome/ID da lista, conteúdo da minuta e objeto processual com os autos. Não inventar IDs nem usar números de outro processo. O assistente-de-minutas existente contém módulos CNT APLV; só executá-los quando confirmada essa variante. Vacina HPV e outros modelos ainda sem skill não recebem regras APLV. Quando faltar skill específica, registrar preenchimento específico pendente e não improvisar regras jurídicas.

Para CNT APLV, ler e aplicar em ordem as skills instaladas:
1. assistente-de-minutas:orquestrador-minutas-cnt-aplv;
2. assistente-de-minutas:preenchimento-basico-minuta-cnt-aplv;
3. assistente-de-minutas:preliminares-minuta-cnt-aplv;
4. assistente-de-minutas:conferencia-final-minuta-cnt-aplv.

Ler referências e bancos aprovados exigidos pelos módulos. Se ausentes, não inventar nem reconstruir o banco; registrar a limitação e continuar tarefas independentes. Novas skills devem definir o roteiro de análise e regras do respectivo modelo antes de habilitar seu preenchimento.

## Dossiê e pareamento

Usar spa_ler_pasta_atual, spa_listar_documentos_autos e spa_ler_documento_autos para obter fatos e evidências. Completar a leitura por paginas quando necessário. Usar spa_identificar_documento_minuta para obter documentoGoogleId, processoId, etapaId e minutaId e a distinção do modelo original. Abrir exatamente esse documento pela conexão Google Drive/Docs do plugin. Quando a conexão exigir URL, construir https://docs.google.com/document/d/{documentoGoogleId}/edit usando somente o ID realmente retornado, sem pedir ao usuário que copie o link. Confirmar CNJ entre autos/SPA e conteúdo dessa minuta. Ler texto, estrutura e formatação pela conexão do plugin, com paginação e revisão consistentes. Não pesquisar ou escolher outro documento se o ID identificado estiver inacessível.

Dossiê separado por processo: CNJ, ID SPA, etapa, minutaId, documento Google, nome/ID do modelo, skill e versão usada, revisões, documentos lidos com ID/páginas/completude, relatório, alterações realizadas, pendências e resultados dos módulos. Dossiê confirmado não comprova leitura dos autos nem aplicabilidade de uma skill. Não reutilizar fatos, relatórios ou planos de outro caso.

Se CNJ na minuta divergir dos autos, ou destino ficar ambíguo: não escrever e pedir esclarecimento de identidade. CNJ ausente/placeholder não é correspondência confirmada; tratar conforme regra explícita da skill e não substituir automaticamente número conflitante. Falta de acesso/escrita é bloqueio técnico; informar sem pedir aprovação para repetir ação inalterada.

## Relatório interno obrigatório

Antes do preenchimento, percorrer todos os itens exigidos pela skill e todos os trechos condicionais do modelo. Para cada item registrar:
- item/campo/tópico e regra da skill;
- dados necessários e documentos a conferir;
- resultado: demonstrado, alegado, não localizado, insuficiente ou contraditório;
- fatos e evidências ID/página, distinguindo alegação de prova;
- completude e limitações da fonte;
- conclusão e ação permitida: preencher, adaptar, manter, excluir, inserir ou preservar como pendência;
- localização do trecho na minuta e limites de formatação;
- confiança e justificativa, sem transformar dúvida em fato.

Analisar identidade/representação, manifestação/fase, objeto e pedidos, decisões, valor da causa/custo, dados médicos, prescrição, tratamentos/alternativas, requerimento administrativo, NAT-Jus, competência, condições do modelo e preliminares do banco conforme a skill. O roteiro é parametrizado pela skill: não exigir ou aplicar todos esses itens em modelos onde não cabem.

Relatório separado da peça. Não pedir sua revisão. Não inserir pendências internas na minuta. Não selecionar tese apenas por título. Ausência de documento não prova inexistência do fato; falha de extração não prova ilegibilidade. Referências do modelo de outros casos não são fatos deste caso.

## Preenchimento e capacidades da conexão do plugin

Cada alteração deve apontar para uma regra expressa e linha do relatório com evidência suficiente, ou decisão residual expressa. Dúvidas sem regra de edição: preservar o trecho e continuar tarefas independentes. Não interromper para pedir autorização de ampliar a redação.

Usar as ferramentas Google Docs da conexão google_drive do plugin para as alterações autorizadas, no mesmo documento identificado. No fluxo autorizado, não pedir revisão do relatório ou das propostas internas. Se a revisão mudar, reler e reavaliar; não reaplicar cegamente. Não repetir escrita de resultado indeterminado. Não acionar spa_preparar_alteracoes_minuta nem spa_aplicar_alteracoes_minuta nesse fluxo padrão; seu uso direto exige escolha expressa dessa via pelo usuário.

Verificar as capacidades reais da conexão Google Drive/Docs: não presumir que a instalação permita escrita, exclusão de imagens, tabelas ou estilos. Se a skill exigir operação indisponível, registrar a limitação e continuar tarefas independentes. Não simular exclusão estrutural por remoção parcial de texto, nem declarar o fluxo integral concluído se verificação crítica estiver pendente. Nunca criar nova cópia para contornar falta de acesso ao documento identificado.

## Conferência e saída

Comparar autos, relatório e minuta atualizada: identidade; aplicação de cada regra; ausência de invenções; trechos fixos preservados; pedidos conforme regras; fontes e paginação; estrutura e atributos da API quando acessíveis. Conferência textual não equivale a validação visual de imagens/layout.

Resultados por módulo: CONCLUÍDO, REVISÃO NECESSÁRIA ou BLOQUEADO; alterações realizadas; evidências; pendências. Ao final, resumo único e conciso de mudanças/pendências, status por módulo e referência da mesma minuta quando disponível. Não entregar relatório integral salvo pedido. Não declarar aptidão para protocolo com pendências críticas.

## Navegação automática no mesmo processo

A autorização para o fluxo completo inclui a navegação necessária no mesmo processo, a seleção inequívoca em editor vazio, o relatório interno, o preenchimento e a conferência. Execute sem perguntas intermediárias sobre essas etapas. Preserve a exigência de autorização específica para substituir conteúdo existente. A preferência por poucas mensagens não impede informar bloqueios e resultado final.

Ao abrir Documentos Externos, a extensão 0.8.3 registra em memória a página de origem e os autos associados na aba vinculada. Use `spa_abrir_elaboracao_atual` para retornar automaticamente à página de origem e abrir seu único link de elaboração; `spa_retornar_processo` apenas retorna à página do processo. Espere e confira o estado antes de continuar. Contexto ausente, outra aba, autos diferentes, redirecionamento ou link ausente/ambíguo bloqueiam a navegação dependente; não adivinhe IDs ou use outra ferramenta para contornar um bloqueio. Uma nova conexão/reinício requer observar o processo de origem novamente. Downloads e leituras dos autos continuam independentes de elaboração aberta.

Para modelos Fora do SUS cadastrados, leia `assistente-de-minutas:orquestrar-minutas-fora-sus`, seu catálogo e a skill temática correspondente. Confirme com os autos e a minuta; execute preenchimento, condições temáticas, preliminares e conferência na ordem do orquestrador, pelo mesmo assistente, sem subagentes. APLV mantém seu fluxo exclusivo. O assunto cadastrado sozinho não confirma o modelo.

Não tornar o processo de teste uma configuração fixa nem salvar seus dados nas instruções. Atualizar os fontes e os ZIPs no GitHub não atualiza a instalação Windows/Chrome, o túnel nem o plugin já instalado; confirmar a versão pelo handshake MCP e testar o retorno real após instalação.

A rota `/procedures/ID/folder` é a pasta documental; o botão de elaboração fica na página de ações `/procedures/ID`. Preservar a URL de origem observada ao abrir os autos. Se estiver na pasta, seguir o link SPA existente para a página de ações do mesmo ID antes de procurar a elaboração; ausência de link seguro bloqueia a ação. Nunca construir associação por número CNJ nem navegar para outro processo.

## Seleção inicial em Google Docs embutido — 0.8.4

A identificação de uma minuta salva é necessária para editar ou substituir essa minuta; não é pré-requisito para a seleção inicial explicitamente autorizada. Se a inspeção retornar `selecaoInicialGoogleDocsPossivel=true`, houver modelo inequívoco e ordem para selecioná-lo no processo/etapa atuais, executar `spa_selecionar_modelo` com IDs/nome observados, `autorizarEditorGoogleDocs=true`, `autorizarSubstituicao=false` e sem `minutaId`. A possibilidade significa formulário sem minuta salva identificada e único Google Docs reconhecido; não significa editor vazio ou ausência de rascunho não salvo.

Não usar esse modo com minuta salva, IDs conflitantes, mais de um editor ou iframe desconhecido. Substituição de minuta existente conserva os três requisitos anteriores: autorização específica, `minutaId` exato, `autorizarEditorGoogleDocs=true` e `autorizarSubstituicao=true`. A ferramenta bloqueia nova seleção inicial no mesmo formulário depois de um clique solicitado: verificar o resultado sem repetir. Após o clique, identificar e parear a cópia antes de escrever; se a identificação ainda não existir, registrar o bloqueio de edição. Seleção não confirma aplicação nem autoriza salvamento do formulário, assinatura ou protocolo.

## Inspeção e cliques por referência — 0.9.0

Quando precisar entender a interface atual, usar `spa_inspecionar_pagina`. O resultado é um snapshot DOM de títulos e controles visíveis, com `snapshotId`, referências `e1`, `e2` etc., ações reconhecidas, motivos de bloqueio e indicação de incompletude. Não é screenshot nem árvore completa de acessibilidade do Chrome; não lê iframe, HTML bruto, valores de campos, cookies ou rede.

Para uma ação já autorizada, usar `spa_clicar_elemento` com `snapshotId`, `ref` e `autorizarAcao=true`. Não pedir nova aprovação para navegação/seleção já abrangida pelo fluxo. Ref não é seletor CSS e nunca deve ser inventada. Após qualquer ação, obter nova inspeção e verificar o estado; snapshot válido por 60 s, consumido pela ação e invalidado por mudança de rota, sessão ou elemento. Clique solicitado não comprova aplicação. Não repetir clique com resultado indeterminado.

O clique de modelo é encaminhado à mesma validação de `spa_selecionar_modelo`, incluindo seleção inicial ou substituição de minuta conforme as autorizações específicas. Essa via não contorna bloqueios nem permite salvar formulário SPA, assinar ou protocolar. Navegação por referência limita-se a links observados do mesmo processo; navegação para fora de editor, downloads, preenchimento, submissões e ações não classificadas continuam usando ferramentas específicas. Google Drive/Docs permanece a via de edição da minuta.

## Cópia recém-criada sem minuta SPA salva — 0.9.1

`spa_identificar_documento_minuta` pode identificar a cópia Google Docs antes de existir `edited_progress_id`. A ferramenta confere processo/etapa, único iframe, campos da cópia e original e ID Google coincidente e diferente do modelo-fonte. Nesse caso retorna `minutaId:null`, `tipoMinuta:nova` e `minutaSalvaNoSpa:false`. Não inventar ID SPA, não salvar formulário para obter um ID e não repetir a seleção de modelo para verificar. A ausência de ID salvo não impede o uso do documento Google inequivocamente identificado.

Antes de escrever, conferir número processual, texto, estrutura, revisão e regras da skill na mesma cópia pela conexão Google Drive/Docs. A identificação não comprova permissão nem pareamento; número ausente/conflitante segue as regras já existentes. Contexto ambíguo, cópia igual ao original ou campo/iframe divergentes bloqueiam. Manter os campos reais do dossiê; salvar a minuta no SPA não faz parte da identificação.

## Navegação agrupada — 0.9.3

Depois de ler os autos, escolher o modelo e confirmar a skill específica, preferir `spa_preparar_elaboracao` quando exposta. Informar processoId interno observado, id/nome exatos do modelo e caminhoPastas com pares id/nome observados, quando necessário. etapaId é opcional, mas, quando conhecida, deve ser informada. Não inventar IDs ou inferir a escolha pelo assunto; sem catálogo suficiente, usar primeiro as ferramentas de inspeção/listagem existentes. Uma falha do comando agrupado não autoriza contornar bloqueios.

O fluxo agrupa retorno dos autos com origem observada, passagem da pasta para a página de ações, abertura da elaboração e modal, percurso explícito de pastas e seleção inicial. `autorizarAcao=true` deve estar coberto pelo pedido de navegação/seleção. `autorizarEditorGoogleDocs=true` apenas no modo de seleção inicial previamente autorizado, nunca para substituir uma minuta existente. O comando agrupado não aceita autorizarSubstituicao nem minutaId e não é a via de substituição. Mantém as validações dos comandos avulsos.

Examinar etapas, selecaoSolicitada, aplicacaoConfirmada e prontoParaPareamento. Se seleção foi solicitada sem identificação confirmada da nova cópia, reinspecionar e usar spa_identificar_documento_minuta; não repetir a seleção nem preencher por suposição. Falha/timeout após iniciar clique tem resultado indeterminado e não autoriza repetição automática. O comando devolve etapas concluídas em falhas tratadas; desconexão pode impedir recebê-las.

Quando retornar documento, usar exatamente documento.documentoGoogleId como destino para pareamento, leitura, preenchimento e conferência pela conexão Google Drive/Docs do plugin. A cópia identificada ainda exige CNJ e revisão confirmados; prontoParaPareamento não significa pronta para preencher nem minuta concluída. Manter a sequência e regras jurídicas das skills específicas, sem subagentes, assinatura, protocolo ou salvamento de formulário SPA. Não usar a API direta da Triagem como alternativa automática. Atualizar o pacote de skill não atualiza sozinho o MCP instalado; usar o fluxo avulso apenas quando a ferramenta agrupada estiver ausente, respeitando os mesmos bloqueios.
