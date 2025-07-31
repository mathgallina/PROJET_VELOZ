# Sistema de Metas - Veloz Fibra

## 📋 Visão Geral

O sistema de metas da Veloz Fibra é uma ferramenta completa para gerenciamento de metas de vendas e comissões, integrada ao projeto principal `projet_veloz`. O sistema implementa as regras específicas de comissão da empresa e oferece funcionalidades completas de CRUD.

## 🎯 Funcionalidades Principais

### Dashboard de Metas
- **Cards informativos**: Total de metas, concluídas, em andamento e atrasadas
- **Progresso geral**: Taxa de conclusão e progresso médio
- **Faturamento total**: Comissões acumuladas
- **Regras de comissão**: Exibição das regras da Veloz Fibra

### CRUD Completo
- ✅ **Criar metas**: Formulário completo com validação
- ✅ **Visualizar detalhes**: Página detalhada com progresso e informações
- ✅ **Editar metas**: Atualização de todos os campos
- ✅ **Excluir metas**: Confirmação antes da exclusão
- ✅ **Atualizar progresso**: Interface dedicada para progresso

### Relatórios
- 📊 **Relatório em PDF**: Geração de relatórios para impressão
- 📈 **Dados estruturados**: Informações organizadas para análise

## 💰 Regras de Comissão - Veloz Fibra

### Renovações de Contrato
- **Valor**: R$ 3,00 por renovação
- **Meta mínima**: 100 renovações para comissão
- **Cálculo**: `comissão = (renovações >= 100) ? renovações * 3.0 : 0`

### Upgrades de Clientes
- **Valor**: Diferença adicional paga pelo cliente
- **Cálculo**: `comissão = valor_adicional_pago`

### Faturamento Total
- **Percentual**: 5% do faturamento
- **Cálculo**: `comissão = faturamento * 0.05`

### Outros Tipos
- **Novos Clientes**: Metas de quantidade
- **Satisfação do Cliente**: Metas de percentual

## 🏗️ Estrutura Técnica

### Blueprint: `goals`
- **URL Prefix**: `/admin/goals`
- **Registro**: Automático no `app/__init__.py`

### Arquivos Principais
```
app/modules/goals/
├── __init__.py
├── routes.py              # Rotas e endpoints
├── models/
│   ├── __init__.py
│   └── goal.py           # Modelo de dados
├── repositories/
│   ├── __init__.py
│   └── goal_repository.py # Persistência JSON
├── services/
│   ├── __init__.py
│   └── goal_service.py   # Lógica de negócio
└── templates/
    ├── index.html        # Dashboard principal
    ├── create.html       # Criar meta
    ├── show.html         # Visualizar meta
    ├── edit.html         # Editar meta
    └── progress.html     # Atualizar progresso
```

### Dados
- **Arquivo**: `app/data/goals.json`
- **Formato**: JSON estruturado
- **Backup**: Integrado ao sistema de backup

## 🚀 Como Usar

### 1. Acesso ao Sistema
```
URL: http://localhost:8001/admin/goals
Login: admin / admin123
```

### 2. Criar Nova Meta
1. Clique em "Nova Meta"
2. Preencha os campos obrigatórios:
   - **Título**: Nome da meta
   - **Tipo**: Renovações, Upgrades, etc.
   - **Valor Alvo**: Meta a ser atingida
   - **Responsável**: Quem vai executar
   - **Datas**: Início e fim da meta
3. Clique em "Criar Meta"

### 3. Acompanhar Progresso
1. Na lista de metas, clique em "Visualizar"
2. Veja o progresso atual e percentual
3. Clique em "Atualizar Progresso" para modificar

### 4. Gerar Relatório
1. No dashboard, clique em "Gerar Relatório"
2. O sistema gera dados estruturados
3. Implemente geração de PDF conforme necessário

## 📊 Tipos de Meta

| Tipo | Descrição | Cálculo de Comissão |
|------|-----------|---------------------|
| `renewals` | Renovações de Contrato | R$ 3,00 × quantidade (mín. 100) |
| `upgrades` | Upgrades de Clientes | Diferença adicional paga |
| `revenue` | Faturamento Total | 5% do faturamento |
| `new_customers` | Novos Clientes | Metas de quantidade |
| `customer_satisfaction` | Satisfação do Cliente | Metas de percentual |

## 🔧 Configuração

### Variáveis de Ambiente
```bash
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
PORT=8001
```

### Dependências
O sistema utiliza as dependências já instaladas no projeto principal:
- Flask
- Flask-Login
- WTForms
- Jinja2

## 🧪 Testes

### Executar Testes
```bash
# Executar todos os testes
python -m unittest tests/test_goals.py

# Executar teste específico
python -m unittest tests.test_goals.TestGoalModel.test_commission_calculation
```

### Cobertura de Testes
- ✅ Modelo de dados (Goal)
- ✅ Cálculo de comissões
- ✅ Progresso e status
- ✅ Repositório (persistência)
- ✅ Serviço (lógica de negócio)

## 📈 Métricas e KPIs

### Dashboard Principal
- **Total de Metas**: Número total de metas criadas
- **Concluídas**: Metas com status "completed"
- **Em Andamento**: Metas com status "in_progress"
- **Atrasadas**: Metas com prazo vencido
- **Taxa de Conclusão**: Percentual de metas concluídas
- **Progresso Médio**: Média do progresso de todas as metas
- **Faturamento Total**: Soma de todas as comissões

### Alertas Automáticos
- ⚠️ **Metas Atrasadas**: Exibição visual de metas vencidas
- ⏰ **Dias Restantes**: Contador de dias para conclusão
- 📊 **Progresso Baixo**: Alertas para metas com baixo progresso

## 🔒 Segurança

### Autenticação
- Todas as rotas requerem login
- Verificação de permissões via Flask-Login
- Sessões seguras

### Validação de Dados
- Validação de formulários com WTForms
- Sanitização de entrada
- Prevenção de injeção

## 🚨 Troubleshooting

### Problemas Comuns

#### 1. Erro de Importação
```bash
# Verificar se o blueprint está registrado
python -c "from app import create_app; app = create_app(); print('Blueprint registrado')"
```

#### 2. Dados não Carregam
```bash
# Verificar arquivo de dados
cat app/data/goals.json
```

#### 3. Erro de Template
```bash
# Verificar se templates existem
ls app/templates/goals/
```

### Logs
Os logs são exibidos no console durante a execução:
```bash
python app.py
```

## 🔄 Integração

### Menu Principal
O link "Metas" foi adicionado ao menu principal em `app/templates/base.html`

### Sistema de Backup
O sistema de metas está integrado ao sistema de backup existente

### Analytics
Os dados de metas podem ser integrados ao sistema de analytics

## 📝 Changelog

### v1.0.0 (2024-01-XX)
- ✅ Sistema de metas completo
- ✅ Regras de comissão da Veloz Fibra
- ✅ CRUD completo
- ✅ Dashboard responsivo
- ✅ Testes unitários
- ✅ Documentação completa

## 👥 Contribuição

Para contribuir com o sistema de metas:

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Adicione testes
5. Faça commit com mensagem clara
6. Abra um Pull Request

## 📞 Suporte

Para suporte técnico ou dúvidas sobre o sistema de metas:

- **Email**: suporte@velozfibra.com
- **Documentação**: Este arquivo
- **Issues**: Repositório do projeto

---

**Desenvolvido por**: Matheus Gallina  
**Versão**: 1.0.0  
**Licença**: MIT  
**Empresa**: Veloz Fibra 