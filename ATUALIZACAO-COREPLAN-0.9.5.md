# Coreplan 0.9.5 — percurso e continuidade por skill

## O que foi implementado

A extensão Chrome acrescenta **Conectar percurso à IA (navegar e selecionar)**. Esse modo habilita spa_preparar_elaboracao no novo domínio, pelo contrato do MCP 0.9.3 já instalado. Conectar leitura à IA continua somente leitura. Habilitar o modo não executa o percurso por si só: o comando deve ser emitido pela IA dentro da ordem autorizada do usuário.

O percurso usa apenas controles e links observados: processo alvo, próximo passo, Elaborar petição - TJ 1º Grau, Modelos de documentos, pastas exatas e seleção do modelo. Processo, etapa, modelo, nome e cópia Google são conferidos. Os IDs são internos observados, nunca inferidos do CNJ. Não abre endereços construídos nem aceita código/seletores arbitrários. Rotas/atributos ainda não reconhecidos interrompem o fluxo; não há clique por aproximação.

Depois da seleção, confere cópia diferente da anterior, nome do modelo nos metadados e distinção do original. Só retorna prontoParaPareamento=true com identificação concordante. O registro de tentativa é anterior ao clique. Sinal de minuta salva, conteúdo local, contexto divergente, modelo preexistente ou tentativa anterior bloqueiam. Não repetir seleção após resultado indeterminado, mesmo após reinício/reinstalação. Esta versão não substitui minutas existentes.

## Continuidade automática pela IA

O pacote de plugin atualiza fluxo-triagem-minutas e suas referências. Após a identificação e o pareamento com os autos, a IA lê e executa a skill correspondente sem outra chamada do usuário, desde que a ordem inicial inclua preenchimento. Para o modelo Dieta Enteral + Sonda Botton do catálogo conferido, o encaminhamento é contestacoes-fora-do-sus:orquestrar-contestacoes-fsus, perfil dieta-enteral-botton.

A extensão não executa skills no Windows, não chama a API do ChatGPT e não inicia escrita sem a IA na conversa. A skill indicada precisa estar instalada/disponível, assim como Google Drive/Docs. As matrizes dos catálogos são protegidas; o destino é a cópia identificada no SPA. A ausência de informações não autoriza inventar fatos ou regras de edição.

O índice inicial contém apenas o caminho/modelo estrutural já observado. Outros modelos exigem cadastro inequívoco de caminho, IDs e skill após análise dos autos. Dieta enteral não vira padrão para todos os processos. O índice não armazena CNJ, ID interno de processo, expediente, cópia Google ou dados médicos do caso de teste.

## Pacotes separados

- triagem-coreplan-diagnostico-0.9.5.zip: extensão Chrome; mesma identidade, permissões e motor OCR. Extraia em pasta nova e carregue aquela que contém manifest.json. Não regenere a instalação antiga nem altere túnel/Native Messaging.
- triagem-assistente-minutas-plugin-0.9.5.zip: instruções de coordenação, índice e skill de continuidade. Preserva a identidade e a referência ao app existente; inclui manifesto portátil plugin.json e overlay legado .codex-plugin/plugin.json. O ZIP no GitHub não atualiza automaticamente o plugin instalado na conta.

## Validação e limites reais

A seleção local da 0.9.4.11 foi confirmada visualmente pelo usuário; a cópia foi identificada pelo SPA e acessada pelo Google Drive e Google Docs. Nenhum conteúdo foi preenchido nesse teste. Não reutilizar o processo já selecionado para testar seleção de novo.

Na 0.9.5, 219 testes automatizados passaram. Os testes simulados cobrem percurso, validação do contrato 0.9.3, seleção única, cópia nova, limites, divergências, opt-in, tentativa persistente na sessão e skill de continuidade. A sequência completa no novo SPA real e o preenchimento pela skill ainda não foram validados. Não declarar o percurso integral ou a redação concluídos com base nesses testes.

Abertura do processo exige link/identidade reconhecidos na aba vinculada. Esta versão não faz retorno automático de outra janela de autos sem contexto de origem observado. Leitura documental permanece limitada ao PDF já aberto; OCR continua local por página no popup. Não acrescenta leitura automática de todos os autos, salvamento SPA, assinatura ou protocolo.

A atualização só fica ativa no Chrome após carregar o ZIP, e nas futuras conversas após instalar/atualizar a skill de coordenação pelo fluxo do plugin. Primeiro conferir versão e capacidades, depois validar em etapas, sem escrever no documento atual apenas para demonstrar o gatilho.
