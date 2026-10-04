# Alinhamento da candidata do site — 04/10/2026

Escopo: páginas e documentação do site Milhon, com CI estático. A versão publicada permanece na `main` até revisão e coordenação de publicação. Esta é uma revisão editorial e técnica, não um parecer legal. O aplicativo e seus cadastros na Apple não são alterados neste lote.

## Modelo confirmado para esta candidata

As ferramentas de uso são pagas e exigem licença válida. Compra, restauração, termos, privacidade e suporte ficam acessíveis antes da licença. Mensal, anual e vitalício dão acesso ao mesmo conjunto de ferramentas, com modalidades de acesso diferentes. Os identificadores abaixo são os encontrados na fonte do app; esta conferência não comprova o estado dos produtos no App Store Connect.

| Modalidade | Identificador na fonte | Tipo na integração |
| --- | --- | --- |
| Mensal | `com.leonardo.milhon.acesso.mensal` | Assinatura renovável, mensal |
| Anual | `com.leonardo.milhon.acesso.anual` | Assinatura renovável, anual |
| Vitalício | `com.leonardo.milhon.acesso.vitalicio` | Compra não consumível, sem renovação automática |

O preço exibido vem de `Product.displayPrice`/`precoLocalizado`. Não se copiam valores ou cálculos de economia de protótipos para o site. O gateway examinado permite compra somente em Xcode StoreKit Testing ou Sandbox e recusa produção. O site descreve a modalidade em preparação, sem declarar lançamento ou cobrança ativa.

Fonte fixa: [PR #45 do aplicativo](https://github.com/NOOB-debug-cyber/milhon-app/pull/45), examinado no SHA `bbd88c7f672e0056ccfe29b15514e390fbe25116`. A referência é uma candidata em qualificação, não uma versão distribuída. Foram consultados, nesse SHA, os seguintes grupos:

| Informação | Fontes do app |
| --- | --- |
| IDs, tipos e preço localizado | [`catalogoCompras.js`](https://github.com/NOOB-debug-cyber/milhon-app/blob/bbd88c7f672e0056ccfe29b15514e390fbe25116/src/composition/catalogoCompras.js), [`MilhonStoreKitModule.swift`](https://github.com/NOOB-debug-cyber/milhon-app/blob/bbd88c7f672e0056ccfe29b15514e390fbe25116/modules/milhon-storekit/ios/MilhonStoreKitModule.swift), [`MilhonStoreKitGateway.swift`](https://github.com/NOOB-debug-cyber/milhon-app/blob/bbd88c7f672e0056ccfe29b15514e390fbe25116/modules/milhon-storekit/ios/Core/MilhonStoreKitGateway.swift), `PlanosScreen.js` |
| Acesso e operações antes da licença | [`App.js`](https://github.com/NOOB-debug-cyber/milhon-app/blob/bbd88c7f672e0056ccfe29b15514e390fbe25116/App.js), `PlanosScreen.js`, `src/application/comprasMilhon.js`, `src/domain/comprasMilhon.js` |
| Dados de compra no aparelho | `MilhonStoreKitGateway.swift`, `StoreKitBridgeValues.swift`, `src/application/comprasMilhon.js`: produto, transação, datas e estados; direitos em memória, sem storage na aplicação de compras |
| Acervo e backup separados da licença | `src/storage/persist.js`, `backup.js`, `arquivosBackup.js`: dados locais; JSON de acervo; cópia temporária para compartilhamento no aparelho; destino escolhido pelo usuário |
| Fonte pública e diagnóstico | `src/infrastructure/caixaClient.js`, `diagnostico.js`, `App.js`: consultas à CAIXA após acesso autorizado; diagnóstico limitado em memória, sem telemetria automática ou identificadores de compra |
| Privacidade declarada e URLs | [`politicaPublicacao.js`](https://github.com/NOOB-debug-cyber/milhon-app/blob/bbd88c7f672e0056ccfe29b15514e390fbe25116/src/domain/politicaPublicacao.js), `app.json`, `app.config.js`, `package.json`, documentos comerciais e de privacidade |

Esse inventário de fonte fundamenta a candidata textual. Ele não substitui a conferência do IPA final, dos manifests de SDK, de App Privacy ou dos produtos efetivos da loja. Não se declara ausência absoluta de tratamento de dados: Apple, CAIXA, hospedagem, destino de backup e contato de suporte têm fluxos próprios.

## URLs e metadados

As cinco páginas têm descrição específica e URL canônica HTTPS no domínio existente. A home usa a raiz `/milhon-site/`; termos, privacidade, comercial e suporte mantêm os arquivos `.html`. O [README](../README.md) contém o mapa completo para os metadados da loja. Não foi inventado link de produto na App Store.

Os [itens 1.5 e 2.1 das diretrizes de revisão Apple](https://developer.apple.com/app-store/review/guidelines/) foram consultados para contato de suporte e URLs funcionais. O estado de candidata e os pontos ainda em preparação precisam ser resolvidos antes de tratar estes textos como metadados finais de uma submissão.

`URLS_MILHON.site`, `termos` e `privacidade` no app correspondem às URLs canônicas do site. `URLS_MILHON.suporte` ainda é `mailto:cabralmoreirao23@icloud.com`: é um contato funcional, não a página HTTPS de suporte. A coordenação do app precisa decidir a navegação nativa e confirmar `https://noob-debug-cyber.github.io/milhon-site/suporte.html` no campo de suporte da loja. Nenhum campo do App Store Connect foi lido ou alterado por este lote.

Os documentos do app `APP-STORE-METADATA-PT-BR.md`, `PRIVACY-POLICY-DRAFT.md` e `APRESENTACAO-E-PLANOS.md` ainda contêm afirmações anteriores à integração, como ausência de pagamentos/StoreKit ou preços fixos de protótipo. Precisam ser alinhados na etapa do app: pagamento de acesso pela Apple deve ser distinguido de pagamentos de apostas, que não são oferecidos. Não copiar essas afirmações antigas para a candidata do site.

## Lacunas precisas antes da oferta final

| Ponto | O que ainda precisa de confirmação coordenada |
| --- | --- |
| Alcance do vitalício | Redação final do direito de acesso, futuras versões e manutenção, sem transformar um nome de produto em promessa contratual não definida |
| Mudança entre modalidades | Tratamento de assinatura existente ao adquirir vitalício e demais transições, sem prometer cancelamento, crédito, conversão ou reembolso automático |
| Oferta efetiva | Disponibilidade, territórios, produtos aprovados e preços localizados retornados pela Apple; este lote não define ou altera preços, grupos ou níveis |
| Versão distribuível e privacidade | Revalidar os fluxos contra o artefato final e conferir manifests/App Privacy; a descrição não comprova qualificação de produção |
| Metadados da loja | Confirmar URLs de termos, privacidade e suporte HTTPS, descrição paga e contato no portal, além da revisão dos documentos do app |
| Publicação dos textos | Revisar os termos, retirar o estado de candidata apenas quando autorizado e publicar em coordenação com a versão correspondente; a `main` atual permanece preservada |

## Fontes externas consultadas em 04/10/2026

A distinção entre assinatura renovável e compra não consumível segue os [tipos de compra da Apple](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types/). A apresentação de duração, preço localizado, restauração e links legais foi confrontada com a [orientação Apple para assinaturas](https://developer.apple.com/app-store/subscriptions/). Não se configura produto ou mudança de nível com base nesta nota.

As orientações de atendimento remetem aos guias Apple de [cancelamento](https://support.apple.com/pt-br/118428), [restauração](https://support.apple.com/pt-br/108096) e [reembolso](https://support.apple.com/pt-br/118223). A candidata mantém o atendimento pelo responsável e os direitos aplicáveis, sem prometer decisões ou prazos da Apple.

A revisão preserva informação clara e direitos obrigatórios conforme o [CDC, especialmente arts. 30, 31, 46 e 49](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm), sem criar cláusulas de renúncia. Finalidade, responsável, contato e direitos na política foram confrontados com a [LGPD, especialmente arts. 7, 9, 10, 16 e 18](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). A aplicação jurídica concreta e a oferta final seguem para revisão coordenada.

Os fluxos próprios dos provedores permanecem referenciados nas políticas de [Apple](https://www.apple.com/legal/privacy/) e [GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). O site não adiciona scripts de analytics, anúncios ou formulários.
