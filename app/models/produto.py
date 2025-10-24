"""
Modelo para a tabela produtos
"""

from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base


class Produto(Base):
    """
    Tabela de produtos no banco de dados
    """
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False, index=True)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False, index=True)
    
    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', preco={self.preco})>"