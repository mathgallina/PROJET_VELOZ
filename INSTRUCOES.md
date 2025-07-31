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
