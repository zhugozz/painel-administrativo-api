from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from config import global_settings  # Certifique-se de que sua URL do banco de dados está correta aqui

# Definir a base dos modelos
DBBaseModel = declarative_base()

# Criar o engine assíncrono com a URL de conexão do banco de dados
engine: AsyncEngine = create_async_engine(global_settings.DB_URL, echo=False)

# Configuração da sessão assíncrona
Session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

# Função para criar a sessão de banco de dados (para uso nas rotas do FastAPI, por exemplo)
async def get_db():
    async with Session() as session:
        yield session  # Utilizando o contexto assíncrono
