# Vitivinicultura API

Este projeto cria uma API pública para consultar dados de vitivinicultura da Embrapa, incluindo informações sobre Produção, Processamento, Comercialização, Importação e Exportação.

## Estrutura do Projeto
tech_challenge_api/
├── app/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── csv_reader.py
│ ├── models.py
│ ├── security.py
├── data/
│ ├── raw_data/
│ │ ├── producao.csv
│ │ ├── processamento.csv
│ │ ├── comercializacao.csv
│ │ ├── importacao.csv
│ │ ├── exportacao.csv
├── scrapers/
│ ├── init.py
│ ├── env.py
│ ├── main.py
│ ├── scraper.py
│ ├── utils.py
├── tests/
│ ├── init.py
│ ├── conftest.py
│ ├── test_scraper.py
├── requirements.txt
└── README.md

## Funcionalidades da API

A API possui os seguintes endpoints:
- `/producao` - Consulta dados de produção de vitivinicultura.
- `/processamento` - Consulta dados de processamento de vitivinicultura.
- `/comercializacao` - Consulta dados de comercialização de vitivinicultura.
- `/importacao` - Consulta dados de importação de vitivinicultura.
- `/exportacao` - Consulta dados de exportação de vitivinicultura.

## Requisitos

- Python 3.9+


## Instalação e Configuração
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt


### Clonar o Repositório

```bash
git clone https://github.com/AleksandroSantos/tech_challenge_api.git
cd tech_challenge_api
