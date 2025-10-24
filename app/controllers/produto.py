"""
Controllers para endpoints de produtos
"""

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.schemas.produto import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from app.services.produto import ProdutoService

router = APIRouter(
    prefix="/api/produtos",
    tags=["Produtos"]
)


@router.post(
    "/",
    response_model=ProdutoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar produto"
)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    """Cria um novo produto no sistema """
    return ProdutoService.criar_produto(db, produto)


@router.get(
    "/",
    response_model=List[ProdutoResponse],
    summary="Listar produtos"
)
def listar_produtos(
    categoria: Optional[str] = Query(None, description="Filtrar por categoria"),
    db: Session = Depends(get_db)
):
    """Lista produtos com paginação e filtro opcional por categoria"""
    return ProdutoService.listar_produtos(db, categoria)


@router.get(
    "/{produto_id}",
    response_model=ProdutoResponse,
    summary="Buscar produto por ID"
)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    """Retorna um produto específico pelo ID"""
    return ProdutoService.buscar_produto(db, produto_id)


@router.put(
    "/{produto_id}",
    response_model=ProdutoResponse,
    summary="Atualizar produto"
)
def atualizar_produto(
    produto_id: int,
    produto: ProdutoUpdate,
    db: Session = Depends(get_db)
):
    """Atualiza dados de um produto existente  """
    return ProdutoService.atualizar_produto(db, produto_id, produto)


@router.delete(
    "/{produto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar produto"
)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    """Remove um produto do sistema"""
    ProdutoService.deletar_produto(db, produto_id)