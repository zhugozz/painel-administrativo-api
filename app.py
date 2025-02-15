import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import api_router
from config import global_settings

app = FastAPI(
    title="Painel Administrativo para Empresa",
    version="1.0.0",
    description="API para gerenciar empresas e obrigações acessórias."
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

# Adicionando os routers
app.include_router(api_router, prefix=global_settings.API_V_STR)

# Executando a aplicação
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render define a porta automaticamente
    uvicorn.run("app:app", host="0.0.0.0", port=port, log_level="info", reload=True)
