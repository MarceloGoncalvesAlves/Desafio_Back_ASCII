"""
Schemas para validação e serialização de dados do produto
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class ProdutoBase(BaseModel):
    """Campos base compartilhados entre schemas."""
    nome: str = Field(..., min_length=1, max_length=100, description="Nome do produto")
    preco: float = Field(..., gt=0, description="Preço do produto")
    categoria: str = Field(..., min_length=1, max_length=50, description="Categoria do produto")


class ProdutoCreate(ProdutoBase):
    """Schema para criação de produto"""
    pass


class ProdutoUpdate(BaseModel):
    """Schema para atualização de um produto """
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    preco: Optional[float] = Field(None, gt=0)
    categoria: Optional[str] = Field(None, min_length=1, max_length=50)


class ProdutoResponse(ProdutoBase):
    """Schema de resposta da API, adiciona id"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)