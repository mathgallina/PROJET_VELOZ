# 🚀 Início Rápido - Wiki Veloz Fibra

## ⚡ Execução Rápida

### 1. Clone e Configure
```bash
git clone <url-do-repositorio>
cd projet_veloz
```

### 2. Ambiente Virtual
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar
```bash
bash scripts/start.sh
```

### 5. Acessar
- **URL**: http://localhost:8001
- **Login**: admin / admin

## 📁 Estrutura do Projeto

```
projet_veloz/
├── app/                    # Aplicação Flask
│   ├── core/              # Configurações
│   ├── modules/           # Módulos da aplicação
│   ├── static/            # Arquivos estáticos
│   └── templates/         # Templates HTML
├── scripts/               # Scripts utilitários
├── backups/               # Arquivos de backup
├── requirements.txt       # Dependências
├── app.py                # Ponto de entrada
└── README.md             # Documentação completa
```

## 🔧 Configuração

### Variáveis de Ambiente
```bash
cp env.example .env
# Edite o arquivo .env com suas configurações
```

### Google Drive (Backup)
1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto e ative a Google Drive API
3. Crie credenciais de conta de serviço
4. Baixe o arquivo JSON como `credentials.json`
5. Configure `GOOGLE_DRIVE_FOLDER_ID` no `.env`

## 🎯 Funcionalidades

- ✅ **Dashboard** - Visão geral do sistema
- ✅ **Páginas** - Gerenciamento de conteúdo wiki
- ✅ **Documentos** - Upload e organização de arquivos
- ✅ **Backup** - Sistema automático de backup
- ✅ **Analytics** - Relatórios e estatísticas
- ✅ **Usuários** - Administração de usuários
- ✅ **Notificações** - Sistema de alertas
- ✅ **PDFs** - Gerenciamento de PDFs

## 🚨 Troubleshooting

### Problemas Comuns

1. **Erro de permissão no script**
   ```bash
   chmod +x scripts/start.sh
   ```

2. **Ambiente virtual não encontrado**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Porta já em uso**
   ```bash
   # Mude a porta no arquivo .env
   PORT=8002
   ```

4. **Dependências não instaladas**
   ```bash
   pip install -r requirements.txt
   ```

## 📞 Suporte

- **Documentação**: README.md
- **Issues**: [GitHub Issues]
- **Email**: suporte@velozfibra.com

---

**Wiki Veloz Fibra** - Sistema de Gerenciamento Profissional v1.0.0 