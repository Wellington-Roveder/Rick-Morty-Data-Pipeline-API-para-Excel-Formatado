Descrição

Este projeto automatiza a extração, tratamento e formatação de dados da API do Rick and Morty. A aplicação consome informações de personagens, transforma os dados (incluindo tradução de termos técnicos para o português) e gera um relatório em Excel já estruturado e pronto para uso.

O principal objetivo foi aplicar conceitos de arquitetura limpa e modularização, garantindo que cada camada do sistema (consumo da API, regras de negócio e geração de saída) seja independente, organizada e fácil de manter.

Esse projeto também marca minha evolução prática no consumo de APIs. A partir de um modelo base de estudos, adaptei e evoluí a estrutura para um cenário mais próximo do mundo real, focando em lógica de programação e boas práticas utilizadas no mercado.

Diferenciais Técnicos

Consumo eficiente de API
Utilização de requests.Session() no APIClient, permitindo reutilização de conexões HTTP e melhor desempenho nas requisições.

Tratamento e tradução de dados
O personagem_service.py atua como camada de transformação, convertendo o JSON bruto da API em um formato mais amigável e traduzido (status, gênero, espécie, etc.).
Além disso, centraliza a comunicação com a API, evitando espalhamento de endpoints pelo projeto.

Geração de Excel estruturado
O excel_service.py, utilizando openpyxl, gera um relatório com:

Auto ajuste da largura das colunas
Filtros automáticos no cabeçalho
Congelamento da primeira linha
Estilização do cabeçalho em negrito
Estrutura do Projeto
project/
│
├── api/
│   └── client.py              # Cliente HTTP com Session e timeout
├── services/
│   ├── excel_service.py       # Geração e formatação do Excel
│   └── personagem_service.py  # Regras de negócio e transformação de dados
├── utils/
│   └── logger.py              # Configuração de logs
├── main.py                    # Orquestração do fluxo
└── relatorio_api_exemplo.xlsx # Exemplo de saída
Como executar
Clone o repositório
Crie e ative um ambiente virtual
Instale as dependências:
pip install pandas requests openpyxl
Execute o projeto:
python main.py
Fluxo da aplicação
main.py
   ↓
APIClient (requisições HTTP)
   ↓
JSON bruto
   ↓
personagem_service (tratamento e tradução)
   ↓
excel_service (geração do relatório)
   ↓
arquivo.xlsx
Dificuldades encontradas
Integração com envio via WhatsApp, que ainda está em evolução
Manipulação e formatação avançada de Excel com openpyxl, exigindo bastante pesquisa em documentação
Melhorias futuras
Implementar logging profissional com o módulo logging (níveis, arquivos de log, rastreamento de erros)
Adicionar paralelismo para consumo de múltiplas páginas da API
Integração com WhatsApp para envio automático de relatórios
Evoluir o projeto para cenários reais (financeiro, logístico, etc.)
Objetivos alcançados

Durante o desenvolvimento, consegui aplicar na prática:

Organização de código com foco em Clean Code
Estruturação de um fluxo ETL (extração, transformação e carga)
Boas práticas no consumo de APIs
Separação de responsabilidades entre camadas
Conclusão

Esse projeto foi um passo importante na minha evolução com Python, principalmente no contexto de automação e dados. Mais do que consumir uma API, a proposta foi construir uma solução organizada, escalável e próxima de um cenário real de desenvolvimento.

Atualmente, sigo evoluindo esse modelo com foco em engenharia de dados e automações voltadas para problemas reais de negócio.

Contato

Estou em busca de oportunidades como Desenvolvedor Estagiário ou Júnior.
Fico aberto a feedbacks e trocas de ideia sobre o projeto.

LinkedIn:
https://www.linkedin.com/in/wellington-roveder-04637b37b/
