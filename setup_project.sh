#!/bin/bash

# Wiki Veloz Fibra - Script de Configuração do Projeto
# Autor: Matheus Gallina
# Versão: 1.0.0

set -e  # Exit on any error

echo "🚀 Iniciando configuração do projeto Wiki Veloz Fibra..."

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para log colorido
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se estamos no diretório correto
if [ ! -f "app.py" ]; then
    log_error "Este script deve ser executado no diretório raiz do projeto!"
    exit 1
fi

log_info "Verificando estrutura do projeto..."

# Criar diretórios necessários se não existirem
log_info "Criando diretórios necessários..."
mkdir -p app/static/uploads/documents
mkdir -p app/static/uploads/attachments
mkdir -p backups
mkdir -p logs

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    log_info "Criando ambiente virtual..."
    python3 -m venv venv
    log_success "Ambiente virtual criado"
else
    log_info "Ambiente virtual já existe"
fi

# Ativar ambiente virtual
log_info "Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
log_info "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt
log_success "Dependências instaladas"

# Verificar se o arquivo .env existe
if [ ! -f ".env" ]; then
    log_info "Criando arquivo .env..."
    cat > .env << EOF
# Wiki Veloz Fibra - Environment Variables
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
PORT=8001

# Security
SECRET_KEY=dev-secret-key-change-in-production

# Database (if needed in future)
# DATABASE_URL=sqlite:///app.db

# Backup Configuration
# GOOGLE_DRIVE_FOLDER_ID=your_google_drive_folder_id

# Email Configuration (if needed in future)
# MAIL_SERVER=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USE_TLS=True
# MAIL_USERNAME=your_email@gmail.com
# MAIL_PASSWORD=your_app_password
EOF
    log_success "Arquivo .env criado"
else
    log_info "Arquivo .env já existe"
fi

# Verificar se os arquivos de dados existem
log_info "Verificando arquivos de dados..."
for file in users.json employees.json goals.json activity_log.json; do
    if [ ! -f "app/data/$file" ]; then
        log_warning "Arquivo app/data/$file não encontrado, criando..."
        echo "[]" > "app/data/$file"
    fi
done

# Verificar permissões
log_info "Configurando permissões..."
chmod +x app.py
chmod +x scripts/start.sh

# Testar a aplicação
log_info "Testando a aplicação..."
python -c "
import sys
sys.path.append('.')
from app import create_app
app = create_app()
print('✅ Aplicação Flask criada com sucesso')
"

if [ $? -eq 0 ]; then
    log_success "Teste da aplicação passou"
else
    log_error "Erro ao testar a aplicação"
    exit 1
fi

# Criar script de inicialização
log_info "Criando script de inicialização..."
cat > start_server.sh << 'EOF'
#!/bin/bash

# Wiki Veloz Fibra - Script de Inicialização
echo "🚀 Iniciando Wiki Veloz Fibra..."

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
EOF

chmod +x start_server.sh

# Criar arquivo de instruções
log_info "Criando arquivo de instruções..."
cat > INSTRUCOES.md << 'EOF'
# Wiki Veloz Fibra - Instruções de Uso

## 🚀 Como Iniciar o Projeto

### Opção 1: Script Automático
```bash
./start_server.sh
```

### Opção 2: Manual
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Definir variáveis de ambiente
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_HOST=0.0.0.0
export PORT=8001

# Iniciar servidor
python app.py
```

## 🌐 Acesso ao Sistema

- **URL**: http://localhost:8001
- **Login padrão**: admin / admin123

## 📁 Estrutura do Projeto

```
projet_veloz/
├── app/
│   ├── core/           # Configurações
│   ├── data/           # Arquivos JSON
│   ├── modules/        # Módulos da aplicação
│   ├── static/         # Arquivos estáticos
│   ├── templates/      # Templates Jinja2
│   └── shared/         # Utilitários compartilhados
├── backups/            # Backups do sistema
├── venv/               # Ambiente virtual
├── app.py              # Arquivo principal
├── requirements.txt    # Dependências
└── .env               # Variáveis de ambiente
```

## 🔧 Configurações

### Porta do Servidor
O servidor está configurado para rodar na porta **8001**

### Debug Mode
Debug está ativado por padrão para desenvolvimento

### Estrutura Modular
- **auth**: Autenticação e login
- **main**: Dashboard principal
- **pages**: Gerenciamento de páginas
- **documents**: Sistema de documentos
- **backup**: Sistema de backup
- **analytics**: Analytics e relatórios
- **notifications**: Sistema de notificações
- **pdfs**: Gerenciamento de PDFs
- **users**: Gerenciamento de usuários
- **goals**: Sistema de metas
- **hr**: Recursos humanos

## 🛠️ Desenvolvimento

### Adicionar Nova Funcionalidade
1. Crie um novo módulo em `app/modules/`
2. Siga o padrão: models, repositories, services, routes
3. Registre o blueprint em `app/__init__.py`

### Templates
- Use `{% extends "base.html" %}` para herdar o template base
- Mantenha a estrutura responsiva com Bootstrap 5

## 📝 Logs

Os logs são exibidos no console durante a execução.

## 🔒 Segurança

- Altere a SECRET_KEY em produção
- Configure HTTPS em produção
- Use variáveis de ambiente para credenciais

## 🚨 Troubleshooting

### Erro de Porta
Se a porta 8001 estiver ocupada, altere a variável PORT no .env

### Erro de Dependências
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Erro de Permissões
```bash
chmod +x start_server.sh
chmod +x app.py
```
EOF

log_success "✅ Configuração concluída com sucesso!"
echo ""
echo "🎉 Projeto Wiki Veloz Fibra configurado!"
echo ""
echo "📋 Próximos passos:"
echo "1. Execute: ./start_server.sh"
echo "2. Acesse: http://localhost:8001"
echo "3. Login: admin / admin123"
echo ""
echo "📖 Consulte INSTRUCOES.md para mais detalhes"
echo "" 