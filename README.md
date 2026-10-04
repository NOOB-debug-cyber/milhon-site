# Milhon — páginas públicas

Site informativo, Termos de Uso, Política de Privacidade, Condições Comerciais e Suporte.

Este repositório contém as páginas do site e sua documentação de revisão. A raiz da branch `main` é a versão publicada; candidatas ficam em branches e PRs draft até a revisão coordenada. Não contém o código do aplicativo, dados de usuários, credenciais ou o pacote privado de continuidade.

Responsável: Leonardo Cabral Moreira. Suporte: cabralmoreirao23@icloud.com.

Hospedagem estática pelo GitHub Pages, a partir da raiz da branch `main`. Sem rastreamento próprio, formulários de coleta ou dependências externas de execução. A publicação do site não significa disponibilização do aplicativo na App Store.

Milhon é independente, sem afiliação, patrocínio ou endosso da CAIXA. Não vende apostas nem garante prêmios.

## Modalidades da candidata

O modelo em preparação prevê assinatura mensal, assinatura anual e acesso vitalício por compra não consumível. Todas as ferramentas de uso exigem licença válida; compra, restauração, termos, privacidade e suporte ficam acessíveis antes da licença. Os três planos dão acesso ao mesmo conjunto de ferramentas. Mensal e anual se renovam automaticamente; vitalício é pagamento único, sem renovação automática.

Os preços exibidos no aplicativo vêm da Apple de forma localizada. Este site não fixa preços, processa pagamentos ou anuncia lançamento. Restauração de licença e backup do acervo são operações distintas. O alcance final do vitalício e as condições de transição entre modalidades dependem do alinhamento da oferta antes da distribuição.

## URLs e verificação

| Finalidade | URL pública |
| --- | --- |
| Apresentação | https://noob-debug-cyber.github.io/milhon-site/ |
| Termos de Uso | https://noob-debug-cyber.github.io/milhon-site/termos.html |
| Privacidade | https://noob-debug-cyber.github.io/milhon-site/privacidade.html |
| Condições Comerciais | https://noob-debug-cyber.github.io/milhon-site/comercial.html |
| Suporte | https://noob-debug-cyber.github.io/milhon-site/suporte.html |

Contato: `mailto:cabralmoreirao23@icloud.com`. A página HTTPS de suporte e o contato por e-mail têm finalidades distintas. O link nativo atualmente abre o e-mail; a URL de suporte dos metadados da loja deve apontar para a página HTTPS. A confirmação no App Store Connect pertence à etapa coordenada do aplicativo.

Execute `python3 scripts/check_site.py` para validar a estrutura das cinco páginas, recursos, âncoras, descrições e URLs canônicas. O CI existente também executa `git diff --check` em PRs e na `main`.

A [nota de alinhamento](docs/ALINHAMENTO-PLANOS-2026-10-04.md) registra as fontes confirmadas, as divergências do aplicativo e as lacunas que ainda impedem tratar a candidata como oferta final. Abrir um PR draft não publica o site.
