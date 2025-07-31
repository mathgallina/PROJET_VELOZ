#!/bin/bash

# Wiki Veloz - Script de Inicialização
echo "🚀 Iniciando Wiki Veloz..."

# Ativar ambiente virtual
source venv/bin/activate

# Definir variáveis de ambiente
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_HOST=0.0.0.0
export PORT=8001

# Iniciar servidor
echo "📡 Servidor iniciando na porta 8001..."
echo "🌐 Acesse: http://localhost:8001"
echo "🔑 Login padrão: admin / admin123"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

python app.py
