# Guia de Atualização do Projeto Django na VPS

Este guia descreve os passos necessários para atualizar a aplicação Django na VPS após fazer alterações no código.

## Passos para Atualização

### 1. Navegue até o diretório do projeto

```bash
cd /root/sinto/Sintonize
```

### 2. Ative o Ambiente Virtual (venv)

⚠️ **Importante:** Este passo é crucial para garantir que você está usando os pacotes Python corretos.

```bash
source venv/bin/activate
```

### 3. Baixe as atualizações do GitHub

O comando `git pull` busca e mescla as alterações que você enviou para o repositório.

```bash
git pull origin main
```

### 4. Instale ou atualize as dependências (opcional)

💡 **Execute apenas se:** você adicionou um novo pacote Python e atualizou o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Aplique as migrações do banco de dados (opcional)

💡 **Execute apenas se:** você alterou os arquivos `models.py` do seu projeto.

```bash
python manage.py migrate
```

### 6. Reinicie o Gunicorn

🚀 **Passo final e mais importante:** Este comando reinicia sua aplicação Django, fazendo com que todas as suas alterações de código entrem em vigor.

```bash
sudo systemctl restart gunicorn
```

## ✅ Finalização

Pronto! Seu site na VPS está atualizado com as últimas modificações. 

> 💡 **Dica:** Você não precisa reiniciar o Nginx, a menos que tenha alterado os arquivos de configuração dele.