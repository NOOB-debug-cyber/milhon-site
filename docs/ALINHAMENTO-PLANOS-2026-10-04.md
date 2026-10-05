# Alinhamento do site — revisão documental de 05/10/2026

Escopo: site Milhon e documentação de revisão. A versão publicada permanece na `main` até a revisão do novo delta e a coordenação de publicação. Esta é uma revisão editorial e técnica, não um parecer legal. App, Apple e outros produtos não são alterados neste lote.

## Modelo confirmado

Todas as ferramentas de uso são pagas e exigem licença válida. Compra, restauração, termos, privacidade e suporte ficam acessíveis antes da licença. Os três planos dão acesso ao mesmo conjunto de ferramentas. Não se criam promessas de manutenção permanente, novos serviços, conversão, crédito, reembolso ou cancelamento automático de outra modalidade.

| Modalidade | Identificador na fonte | Natureza do acesso |
| --- | --- | --- |
| Mensal | `com.leonardo.milhon.acesso.mensal` | Assinatura mensal, renovação automática |
| Anual | `com.leonardo.milhon.acesso.anual` | Assinatura anual, renovação automática |
| Vitalício | `com.leonardo.milhon.acesso.vitalicio` | Compra não consumível, pagamento único, sem renovação ou expiração artificial; respeita revogação/reembolso pela Apple |

O preço exibido vem da Apple de forma localizada; o site não copia valores ou cálculos de economia de protótipos. Identificadores encontrados na fonte não comprovam o estado atual dos produtos no App Store Connect. A preparação de produção continua distinta de lançamento, contratação ativa e validação do build distribuído.

## Fontes e compatibilidade

Referência de compatibilidade: [app PR #46](https://github.com/NOOB-debug-cyber/milhon-app/pull/46), SHA `209f6c708bf04634641964332c06254991ee91e0`. Foram relidos dez arquivos de fonte/documentação e o gerador de documentos nesse SHA, sem executar código do app. O inventário anterior de dados locais foi confrontado com o complemento documental de 05/10/2026; o pacote privado não é copiado para este repositório.

| Tema | Fonte confirmada | Resultado para o site |
| --- | --- | --- |
| Licença e preços | `src/composition/catalogoCompras.js`, `src/application/comprasMilhon.js`, `docs/APRESENTACAO-E-PLANOS.md` | Três modalidades, mesmo conjunto de ferramentas, preço localizado e restauração separada do backup |
| Compras nativas | [MilhonStoreKitGateway.swift](https://github.com/NOOB-debug-cyber/milhon-app/blob/209f6c708bf04634641964332c06254991ee91e0/modules/milhon-storekit/ios/Core/MilhonStoreKitGateway.swift) | Sandbox/produção somente com identidade verificada do Milhon; isso não comprova compra real ou qualificação de distribuição |
| Dados de licença | Gateway e `src/application/comprasMilhon.js` | Produto, transação, datas, estados, comparação de identificador original e ambiente; estado de acesso em memória, sem backend próprio de validação ou licença no backup JSON |
| Consulta CAIXA | [App.js](https://github.com/NOOB-debug-cyber/milhon-app/blob/209f6c708bf04634641964332c06254991ee91e0/App.js) | Atualização condicionada ao acesso autorizado, já descrita em privacidade item 3 |
| Diagnóstico | `src/infrastructure/diagnostico.js` | Eventos limitados em memória, sem telemetria automática ou identificadores de compra, já descritos no item 5 |
| Suporte, hospedagem e backups | Manual/política gerados por [build_publication_docs.py](https://github.com/NOOB-debug-cyber/milhon-app/blob/209f6c708bf04634641964332c06254991ee91e0/scripts/build_publication_docs.py), complemento documental e `src/storage/backup.js` | Site já descreve atendimento por e-mail, GitHub Pages, retenção por necessidade e exportação escolhida pelo usuário |
| URLs | [politicaPublicacao.js](https://github.com/NOOB-debug-cyber/milhon-app/blob/209f6c708bf04634641964332c06254991ee91e0/src/domain/politicaPublicacao.js) | Site, termos, privacidade e suporte HTTPS coincidem com o app candidato; o contato por e-mail continua disponível |

Os Markdown históricos `PRIVACY-POLICY-DRAFT.md` e `APP-STORE-METADATA-PT-BR.md` ainda contêm campos ou frases antigas. A documentação gerada no PR #46 distingue pagamento de acesso pela Apple de pagamentos de apostas, que não são oferecidos. Esses Markdown não devem substituir automaticamente os textos finais gerados e reconciliados.

O PR #46 foi integrado com o follow-up `8f2706b3d010ff9d03f87e691a7b595b700ada15`, merge `97e0f346e38abb09b1c033de27543b1a7308fbd8`. A comparação com `209f6c7` contém somente o patch de paginação/banner do gerador e suas referências de integridade no tooling, sem mudança de código de licença, diagnóstico, suporte ou backup. O gerador integrado é idêntico ao overlay do complemento, SHA-256 `37df9995418f8095e4c9b2982bba757871b7644d9ede04f99471565c676ae9c1`.

O complemento identifica ajustes a fazer no DOCX de privacidade: explicitar acesso autorizado na atualização inicial, diagnóstico em memória, atendimento/hospedagem e compartilhamento de backup. Essas informações já existem no site. O patch visual já integrado pertence à coordenação documental do app. A reconciliação do corpo e a remoção da página de controle interno do documento público continuam nessa etapa; este lote não altera o app.

## Data, vigência e publicação

05/10/2026 é a data desta revisão documental, não uma declaração de vigência passada ou de lançamento. Os textos passam a valer quando esta versão for publicada no endereço correspondente. O recibo de deploy deve registrar a data efetiva e confirmar a correspondência com a versão pública dos documentos. Foram retiradas dos textos públicos as instruções de revisão interna; a preparação do aplicativo continua declarada enquanto refletir seu estado real.

As páginas mantêm as URLs HTTPS existentes, descrições específicas e URL canônica. O [README](../README.md) contém o mapa para os metadados da loja. A conferência de suporte/privacidade pública deve comprovar resposta, conteúdo e acesso sem login por navegador permitido; falha de túnel/proxy ou de ferramenta web não comprova indisponibilidade do site.

Antes do merge, revisar o novo delta sobre o SHA de site anteriormente revisto `d4bc3f0f4f36a2e841f6c22b8fe68b59ce2462ad`. Depois da publicação coordenada, conferir os URLs públicos e a data efetiva; a confirmação dos campos no App Store Connect e no build distribuído permanece na etapa do app. Inventário de fonte não substitui IPA final, manifests de SDK, App Privacy ou catálogo efetivo da loja.

## Fontes externas

Os [tipos de compra da Apple](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types/) e a [orientação de assinaturas](https://developer.apple.com/app-store/subscriptions/) fundamentam a distinção de modalidade, duração, preço localizado, restauração e links legais. Não se configura produto, grupo ou nível com base nesta nota.

As orientações de atendimento remetem aos guias Apple de [cancelamento](https://support.apple.com/pt-br/118428), [restauração](https://support.apple.com/pt-br/108096) e [reembolso](https://support.apple.com/pt-br/118223). Permanecem preservados o atendimento pelo responsável e os direitos aplicáveis. A revisão não cria decisões ou prazos de reembolso da Apple.

As referências jurídicas anteriores — [CDC](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm) e [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) — e os links às políticas de [Apple](https://www.apple.com/legal/privacy/) e [GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) permanecem. O delta não introduz cláusulas de renúncia ou uma nova interpretação jurídica.
