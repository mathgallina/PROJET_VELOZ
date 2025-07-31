#!/bin/bash

# Wiki Veloz Fibra - Startup Script
# Versão: 1.0.0
# Autor: Matheus Gallina

echo "🚀 Iniciando Wiki Veloz Fibra..."

# Verificar se estamos no diretório correto
if [ ! -f "app.py" ]; then
    echo "❌ Erro: Execute este script no diretório raiz do projeto"
    exit 1
fi

# Ativar ambiente virtual
echo "📦 Ativando ambiente virtual..."
source .venv/bin/activate

# Verificar se as dependências estão instaladas
echo "🔍 Verificando dependências..."
if ! python -c "import flask" 2>/dev/null; then
    echo "📥 Instalando dependências..."
    pip install -r requirements.txt
fi

# Criar diretórios necessários
echo "📁 Criando diretórios necessários..."
mkdir -p app/data
mkdir -p app/static/uploads/documents
mkdir -p app/static/uploads/attachments
mkdir -p backups

# Verificar se a aplicação pode ser importada
echo "🔧 Testando aplicação..."
if python -c "from app import create_app; app = create_app(); print('✅ Aplicação OK')" 2>/dev/null; then
    echo "✅ Aplicação testada com sucesso!"
else
    echo "❌ Erro ao testar aplicação"
    exit 1
fi

# Definir variáveis de ambiente
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_HOST=0.0.0.0
export PORT=8001

echo "🌐 Iniciando servidor Flask..."
echo "📍 URL: http://localhost:8001"
echo "🔑 Login: admin / admin"
echo ""
echo "📋 Módulos disponíveis:"
echo "   • /goals - Sistema de Metas"
echo "   • /hr - Recursos Humanos"
echo "   • /documents - Documentos"
echo "   • /backup - Backup"
echo "   • /analytics - Analytics"
echo ""

# Iniciar servidor
python app.py 