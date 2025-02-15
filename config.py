from typing import Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Carregar variáveis do .env, se existir
load_dotenv()

class GlobalConfig(BaseSettings):
    """
    Configurações globais carregadas de variáveis de ambiente.
    """
    API_V_STR: str = "/api/v1"

    # Variável do banco de dados
    DB_URL: str  # O Pydantic automaticamente busca do .env ou ambiente

    class Config:
        case_sensitive = True
        env_file = ".env"  # Especifica que as variáveis podem vir de um arquivo .env
        env_file_encoding = "utf-8"

global_settings = GlobalConfig()
