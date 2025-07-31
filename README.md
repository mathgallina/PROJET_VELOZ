# Wiki Veloz Fibra - Sistema de Gerenciamento Empresarial

## 📋 Resumo do Projeto

Sistema Flask modular para gerenciamento empresarial da Veloz Fibra com funcionalidades completas de autenticação, documentos, backup, analytics, recursos humanos e metas.

## 🚀 Configuração Rápida

### Pré-requisitos
- Python 3.9+
- pip
- git

### Instalação Automática
```bash
# Clone o repositório (se aplicável)
# git clone [URL_DO_REPOSITORIO]

# Execute o script de configuração
./setup_project.sh

# Inicie o servidor
./start_server.sh
```

### Instalação Manual
```bash
# 1. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
cp env.example .env

# 4. Iniciar servidor
python app.py
```

## 🌐 Acesso ao Sistema

- **URL**: http://localhost:8001
- **Login padrão**: admin / admin123
- **Porta**: 8001 (configurável via variável PORT)

## 📁 Estrutura do Projeto

```
projet_veloz/
├── app/
│   ├── core/                    # Configurações centrais
│   │   ├── config.py           # Configurações da aplicação
│   │   └── database.py         # Configuração de banco de dados
│   ├── data/                   # Arquivos JSON de dados
│   │   ├── users.json          # Usuários do sistema
│   │   ├── employees.json      # Funcionários
│   │   ├── goals.json          # Metas
│   │   └── activity_log.json   # Log de atividades
│   ├── modules/                # Módulos da aplicação
│   │   ├── auth/              # Autenticação e login
│   │   ├── main/              # Dashboard principal
│   │   ├── pages/             # Gerenciamento de páginas
│   │   ├── documents/         # Sistema de documentos
│   │   ├── backup/            # Sistema de backup
│   │   ├── analytics/         # Analytics e relatórios
│   │   ├── notifications/     # Sistema de notificações
│   │   ├── pdfs/             # Gerenciamento de PDFs
│   │   ├── users/            # Gerenciamento de usuários
│   │   ├── goals/            # Sistema de metas
│   │   ├── hr/               # Recursos humanos
│   │   └── activity/         # Log de atividades
│   ├── shared/                # Utilitários compartilhados
│   │   ├── decorators.py     # Decoradores customizados
│   │   ├── exceptions.py     # Exceções customizadas
│   │   └── utils.py          # Utilitários gerais
│   ├── static/                # Arquivos estáticos
│   │   └── uploads/          # Uploads de arquivos
│   └── templates/             # Templates Jinja2
│       ├── base.html         # Template base
│       ├── auth/             # Templates de autenticação
│       ├── main/             # Templates principais
│       ├── goals/            # Templates de metas
│       └── hr/               # Templates de RH
├── backups/                   # Backups do sistema
├── scripts/                   # Scripts utilitários
├── venv/                      # Ambiente virtual
├── app.py                     # Arquivo principal
├── requirements.txt           # Dependências Python
├── setup_project.sh          # Script de configuração
├── start_server.sh           # Script de inicialização
├── env.example               # Exemplo de variáveis de ambiente
└── .env                      # Variáveis de ambiente
```

## 🔧 Configurações

### Variáveis de Ambiente (.env)
```bash
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
PORT=8001
SECRET_KEY=dev-secret-key-change-in-production
```

## 🎯 Funcionalidades Principais

### 🔐 Autenticação e Usuários
- Sistema de login seguro
- Gerenciamento de usuários
- Controle de acesso por roles
- Sessões persistentes

### 📄 Gerenciamento de Documentos
- Upload e download de arquivos
- Categorização de documentos
- Sistema de anexos
- Busca e filtros
- Versionamento

### 💾 Sistema de Backup
- Backup automático para Google Drive
- Criptografia de dados
- Agendamento de backups
- Restauração de dados

### 📊 Analytics e Relatórios
- Dashboard interativo
- Métricas de uso
- Relatórios personalizados
- Exportação de dados

### 👥 Recursos Humanos
- Cadastro de funcionários
- Gerenciamento de departamentos
- Relatórios de RH
- Controle de acesso

### 🎯 Sistema de Metas
- Definição de metas
- Acompanhamento de progresso
- Notificações de prazo
- Relatórios de performance

### 🔔 Notificações
- Sistema de notificações em tempo real
- Configuração de alertas
- Histórico de notificações

### 📱 Interface Responsiva
- Design moderno com Bootstrap 5
- Interface adaptável
- Experiência de usuário otimizada

## 🛠️ Desenvolvimento

### Adicionar Nova Funcionalidade
1. Crie um novo módulo em `app/modules/`
2. Siga o padrão: models, repositories, services, routes
3. Registre o blueprint em `app/__init__.py`

### Estrutura de Módulo
```
module_name/
├── __init__.py
├── models/
│   └── model.py
├── repositories/
│   └── repository.py
├── services/
│   └── service.py
├── routes.py
└── validators.py (opcional)
```

### Templates
- Use `{% extends "base.html" %}` para herdar o template base
- Mantenha a estrutura responsiva com Bootstrap 5
- Siga o padrão de nomenclatura

## 🔒 Segurança

- Autenticação segura com bcrypt
- Proteção CSRF
- Validação de entrada
- Sanitização de dados
- Controle de acesso por roles

## 📝 Logs e Monitoramento

- Log de atividades completo
- Rastreamento de ações do usuário
- Monitoramento de performance
- Alertas de segurança

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

### Problemas de Importação
```bash
# Limpar cache Python
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

## 📚 Documentação Adicional

- `INSTRUCOES.md` - Instruções detalhadas de uso
- `QUICKSTART.md` - Guia de início rápido
- `env.example` - Exemplo de configuração

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## 👨‍💻 Autor

**Matheus Gallina**
- Desenvolvedor Full Stack
- Especialista em Python/Flask
- Criador do Wiki Veloz Fibra

## 📞 Suporte

Para suporte técnico ou dúvidas:
- Email: [seu-email@exemplo.com]
- Documentação: [link-para-docs]

---

**Versão**: 1.0.0  
**Última atualização**: Dezembro 2024  
**Status**: ✅ Produção 