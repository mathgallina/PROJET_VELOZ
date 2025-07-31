# Wiki Veloz Fibra

Sistema de gestão empresarial completo desenvolvido em Flask, com foco em organização, escalabilidade e facilidade de uso.

## 🚀 Funcionalidades

### ✅ Implementadas

#### 📊 Sistema de Metas
- Cadastro e gestão de metas de vendas
- Acompanhamento de progresso em tempo real
- Diferentes tipos de metas (valor, quantidade, novos clientes, satisfação)
- Relatórios e dashboards
- Sistema de notificações para metas atrasadas

#### 👥 Recursos Humanos
- Gestão completa de funcionários
- Controle de departamentos
- Acompanhamento de salários e benefícios
- Relatórios de RH
- Sistema de permissões por departamento

#### 📄 Gestão de Documentos
- Upload e organização de documentos
- Sistema de categorização
- Busca avançada
- Controle de versões

#### 🔄 Sistema de Backup
- Backup automático para Google Drive
- Sincronização de arquivos
- Restauração de dados
- Criptografia de dados sensíveis

#### 📈 Analytics
- Dashboards interativos
- Relatórios personalizados
- Métricas de performance
- Exportação de dados

### 🔄 Em Desenvolvimento

#### 🎓 Sistema de Treinamentos
- Cadastro de treinamentos
- Controle de participação
- Certificados automáticos
- Relatórios de capacitação

#### 🔐 Sistema Avançado de Permissões
- Controle granular por usuário
- Permissões por setor
- Auditoria de acessos
- Integração com LDAP

## 🛠️ Tecnologias

- **Backend**: Flask 2.3.3
- **Frontend**: Bootstrap 5, FontAwesome
- **Banco de Dados**: SQLite (JSON para desenvolvimento)
- **Autenticação**: Flask-Login
- **Formulários**: WTForms
- **Backup**: Google Drive API

## 📦 Instalação

### Pré-requisitos
- Python 3.9+
- pip
- Git

### Passos

1. **Clone o repositório**
```bash
git clone <repository-url>
cd projet_veloz
```

2. **Configure o ambiente virtual**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute o script de inicialização**
```bash
chmod +x scripts/start.sh
./scripts/start.sh
```

## 🚀 Uso

### Inicialização Rápida
```bash
./scripts/start.sh
```

### Acesso ao Sistema
- **URL**: http://localhost:8001
- **Usuário**: admin
- **Senha**: admin

### Módulos Principais

#### Sistema de Metas (`/goals`)
- Criar e gerenciar metas de vendas
- Acompanhar progresso em tempo real
- Visualizar relatórios de performance

#### Recursos Humanos (`/hr`)
- Cadastrar funcionários
- Gerenciar departamentos
- Visualizar estatísticas de RH

#### Documentos (`/documents`)
- Upload e organização de arquivos
- Sistema de busca avançada
- Controle de versões

#### Backup (`/backup`)
- Configurar backup automático
- Sincronizar com Google Drive
- Restaurar dados

## 📁 Estrutura do Projeto

```
projet_veloz/
├── app/
│   ├── core/           # Configurações e utilitários
│   ├── modules/        # Módulos da aplicação
│   │   ├── goals/      # Sistema de Metas
│   │   ├── hr/         # Recursos Humanos
│   │   ├── documents/  # Gestão de Documentos
│   │   ├── backup/     # Sistema de Backup
│   │   └── analytics/  # Analytics
│   ├── shared/         # Componentes compartilhados
│   ├── static/         # Arquivos estáticos
│   └── templates/      # Templates HTML
├── scripts/            # Scripts utilitários
├── backups/            # Arquivos de backup
├── requirements.txt    # Dependências Python
└── app.py             # Ponto de entrada
```

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` baseado no `env.example`:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
PORT=8001

# Google Drive API (para backup)
GOOGLE_DRIVE_FOLDER_ID=your-folder-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# Database (futuro)
DATABASE_URL=sqlite:///app.db
```

### Google Drive API (Backup)

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto
3. Ative a Google Drive API
4. Crie credenciais de serviço
5. Baixe o arquivo JSON
6. Configure no `.env`

## 📊 Funcionalidades por Módulo

### Sistema de Metas
- ✅ CRUD completo de metas
- ✅ Acompanhamento de progresso
- ✅ Relatórios e dashboards
- ✅ Notificações automáticas
- ✅ API REST

### Recursos Humanos
- ✅ Gestão de funcionários
- ✅ Controle de departamentos
- ✅ Estatísticas de RH
- ✅ Relatórios salariais
- ✅ API REST

### Documentos
- ✅ Upload de arquivos
- ✅ Organização por categorias
- ✅ Busca avançada
- ✅ Controle de versões

### Backup
- ✅ Backup automático
- ✅ Sincronização Google Drive
- ✅ Criptografia de dados
- ✅ Restauração

## 🧪 Testes

```bash
# Executar testes básicos
python -m pytest tests/

# Verificar cobertura
python -m pytest --cov=app tests/
```

## 📈 Roadmap

### Versão 1.1 (Próxima)
- [ ] Sistema de Treinamentos
- [ ] Sistema Avançado de Permissões
- [ ] Integração com banco PostgreSQL
- [ ] API completa para todos os módulos

### Versão 1.2
- [ ] Sistema de Notificações em tempo real
- [ ] Dashboard executivo
- [ ] Relatórios avançados
- [ ] Integração com sistemas externos

### Versão 2.0
- [ ] Interface mobile responsiva
- [ ] PWA (Progressive Web App)
- [ ] Microserviços
- [ ] Machine Learning para analytics

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Matheus Gallina**
- Email: [seu-email@exemplo.com]
- LinkedIn: [seu-linkedin]
- GitHub: [seu-github]

## 🙏 Agradecimentos

- Comunidade Flask
- Bootstrap Team
- FontAwesome
- Google Drive API

---

**Wiki Veloz Fibra** - Transformando a gestão empresarial com tecnologia moderna e intuitiva. 