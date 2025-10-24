"""
Arquivo principal da API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine, Base
from app.controllers.produto import router as produto_router

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="API de Gerenciamento de Produtos",
    description="API REST para operações CRUD de produtos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produto_router)


@app.get("/", tags=["Health"])
def root():
    """Health check da API"""
    return {
        "message": "API de Produtos",
        "status": "online",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Endpoint de verificação de saúde"""
    return {"status": "healthy"}