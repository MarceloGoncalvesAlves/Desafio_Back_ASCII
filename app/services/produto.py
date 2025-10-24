"""
Camada de serviço para operações de produtos
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate
from typing import List, Optional
from fastapi import HTTPException, status


class ProdutoService:
    """Serviço responsável pela lógica de negócio de produtos'"""
    
    @staticmethod
    def criar_produto(db: Session, produto: ProdutoCreate) -> Produto:
        """Cria um novo produto no banco de dados """
        try:
            novo_produto = Produto(**produto.model_dump())
            db.add(novo_produto)
            db.commit()
            db.refresh(novo_produto)
            return novo_produto
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar produto: {str(e)}"
            )
    
    @staticmethod
    def listar_produtos(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        categoria: Optional[str] = None
    ) -> List[Produto]:
        """Lista produtos com paginação e filtro por categoria"""
        try:
            query = db.query(Produto)
            
            if categoria:
                query = query.filter(Produto.categoria == categoria)
            
            return query.offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao listar produtos: {str(e)}"
            )
    
    @staticmethod
    def buscar_produto(db: Session, produto_id: int) -> Produto:
        """Busca um produto por ID """
        produto = db.query(Produto).filter(Produto.id == produto_id).first()
        
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Produto com ID {produto_id} não encontrado"
            )
        
        return produto
    
    @staticmethod
    def atualizar_produto(
        db: Session, 
        produto_id: int, 
        produto_update: ProdutoUpdate
    ) -> Produto:
        """Atualiza um produto existente"""
        try:
            produto = ProdutoService.buscar_produto(db, produto_id)
            
            dados_atualizacao = produto_update.model_dump(exclude_unset=True)
            
            for campo, valor in dados_atualizacao.items():
                setattr(produto, campo, valor)
            
            db.commit()
            db.refresh(produto)
            return produto
            
        except HTTPException:
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar produto: {str(e)}"
            )
    
    @staticmethod
    def deletar_produto(db: Session, produto_id: int) -> None:
        """Remoce um produto do banco de dados """
        try:
            produto = ProdutoService.buscar_produto(db, produto_id)
            db.delete(produto)
            db.commit()
        except HTTPException:
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao deletar produto: {str(e)}"
            )