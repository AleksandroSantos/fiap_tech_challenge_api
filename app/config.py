import os


class Settings:
    SECRET_KEY: str = "secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATA_DIR: str = "./data/raw_data/"
    PRODUCAO_FILE: str = os.path.join(DATA_DIR, "Produção.csv")
    PROCESSAMENTO_FILE: str = os.path.join(DATA_DIR, "Processamento.csv")
    COMERCIALIZACAO_FILE: str = os.path.join(DATA_DIR, "Comercialização.csv")
    IMPORTACAO_FILE: str = os.path.join(DATA_DIR, "Importação.csv")
    EXPORTACAO_FILE: str = os.path.join(DATA_DIR, "Exportação.csv")


settings = Settings()
