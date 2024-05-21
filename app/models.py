from pydantic import BaseModel


class Producao(BaseModel):
    produto: str
    quantidade: str
    ano: int


class Processamento(BaseModel):
    cultivar: str
    quantidade: str
    ano: int
    opcao: str
    sem_definicao: str


class Comercializacao(BaseModel):
    produto: str
    quantidade: str
    ano: int


class Importacao(BaseModel):
    países: str
    quantidade: str
    valor: str
    ano: int
    opcao: str


class Exportacao(BaseModel):
    países: str
    quantidade: str
    valor: str
    ano: int
    opcao: str
