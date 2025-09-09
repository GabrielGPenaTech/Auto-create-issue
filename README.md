# GitHub Backlog Creator

## 🚀 Como Usar o Script Python

### 1️⃣ Instalar dependências

```bash
pip install requests python-dotenv
```

### 2️⃣ Criar arquivo config.env

```bash
# Crie o arquivo config.env na mesma pasta do script
touch config.env
```

Adicione no arquivo `.config.env`:

```env
GITHUB_TOKEN=seu_token_github_aqui
REPO_OWNER=FARIT-digital
REPO_NAME=nome-do-repositorio-onde-criar-as-issues
```

### 3️⃣ Obter Token do GitHub

1. Vá em: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Selecione escopo: `repo` (acesso completo a repositórios)
4. Copie o token gerado

### 4️⃣ Executar o script

```bash
python python_github_script.py
```

## 🎯 Principais Recursos do Script

### ✅ Interface amigável
- Contador de progresso
- Mensagens coloridas
- Relatório final detalhado

### ✅ Tratamento de erros
- Validação de token e repositório
- Rate limiting automático
- Retry em caso de falhas

### ✅ Todas as tasks organizadas
- Descrições detalhadas
- Labels categorizadas
- Checklists para acompanhamento
- Estimativas de tempo

### ✅ Configuração flexível
- Via variáveis de ambiente
- Via arquivo config.env
- Fácil personalização

## 📋 Estrutura das Issues Criadas

Cada issue terá:

- **Título**: TASK-XXX com descrição clara
- **Descrição**: Objetivos, critérios de aceitação, estimativas
- **Labels**: Por tipo (backend, frontend, high-priority, etc.)
- **Checkboxes**: Para acompanhar progresso

## 🔗 Após Executar

1. **Acesse**: `https://github.com/seu-host/SEU-REPO/issues`
2. **Vá para o Project**: crie um dashboard para administração das tasks do projeto
3. **Adicione as issues** ao projeto
4. **Organize** nas colunas desejadas

## ⚠️ Requisitos

- **Permissões**: Você precisa ter acesso de escrita ao repositório
- **Token**: Deve ter escopo `repo` habilitado
- **Repositório**: Deve existir no GitHub

## 🔧 Personalizar

Para personalizar o script, você pode:

- Modificar as tasks na função `get_all_tasks()`
- Alterar labels, prioridades ou descrições
- Adicionar assignees automáticos
- Configurar diferentes repositórios
