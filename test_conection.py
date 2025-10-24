"""
Script para testar a conexão com o banco de dados PostgreSQL.
Execute: python test_connection.py
"""

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

print("=" * 50)
print("🔍 TESTANDO CONEXÃO COM O BANCO DE DADOS")
print("=" * 50)

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a URL do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Mostra a URL (escondendo a senha por segurança)
if DATABASE_URL:
    # Mascara a senha para mostrar
    url_parts = DATABASE_URL.split(":")
    if len(url_parts) >= 3:
        senha_parte = url_parts[2].split("@")[0]
        url_mascarada = DATABASE_URL.replace(senha_parte, "***")
        print(f"\n📍 Conectando em: {url_mascarada}")
    else:
        print(f"\n📍 Conectando em: {DATABASE_URL}")
else:
    print("\n❌ ERRO: Variável DATABASE_URL não encontrada no arquivo .env")
    print("\nVerifique:")
    print("1. O arquivo .env existe na raiz do projeto?")
    print("2. A linha DATABASE_URL=... está correta?")
    exit(1)

print("\n⏳ Tentando conectar...\n")

try:
    # Cria o motor de conexão
    engine = create_engine(DATABASE_URL)
    
    # Tenta conectar e executar uma query simples
    with engine.connect() as connection:
        # Testa a conexão executando uma query
        result = connection.execute(text("SELECT version();"))
        versao = result.fetchone()[0]
        
        print("✅ CONEXÃO BEM-SUCEDIDA!")
        print("=" * 50)
        print(f"\n✅ PostgreSQL está funcionando!")
        print(f"📦 Versão: {versao.split(',')[0]}")
        print(f"🗄️  Banco: produtos_db")
        print(f"👤 Usuário: postgres")
        print("\n" + "=" * 50)
        print("🎉 Tudo pronto para continuar!")
        print("=" * 50)
        
except Exception as e:
    print("❌ ERRO AO CONECTAR!")
    print("=" * 50)
    print(f"\n❗ Erro: {e}")
    print("\n🔍 Possíveis causas:")
    print("1. PostgreSQL não está rodando")
    print("   → Abra 'services.msc' e verifique o serviço")
    print("2. A senha no arquivo .env está INCORRETA")
    print("   → Verifique o arquivo .env na raiz do projeto")
    print("3. O banco 'produtos_db' não existe")
    print("   → Execute: psql -U postgres")
    print("   → Depois: CREATE DATABASE produtos_db;")
    print("4. A porta 5432 está bloqueada")
    print("   → Verifique firewall ou antivírus")
    print("\n" + "=" * 50)