# Guia para Configurar Domínio de Produção

Este guia descreve como migrar sua aplicação Django do IP da VPS para um domínio personalizado.

## 🎯 Visão Geral

O processo envolve três áreas principais:
- **Provedor de domínio (DNS)**: Configurar apontamentos
- **Aplicação Django**: Atualizar ALLOWED_HOSTS
- **Servidor web Nginx**: Configurar server_name

---

## Passo 1: Configurar DNS

🌐 **Local:** Painel do provedor onde você comprou o domínio (Hostinger, GoDaddy, Registro.br, etc.)

### 1.1 Acesse o Painel de Controle
Encontre a seção chamada **"Gerenciamento de DNS"** ou **"Editor de Zona DNS"**.

### 1.2 Crie os Registros Tipo A
Você precisa criar dois apontamentos para direcionar seu domínio ao IP da VPS:

**📍 Registro 1 (Domínio Raiz):**
- **Tipo:** A
- **Nome/Host:** `@` (ou deixe em branco)
- **Valor/Aponta para:** `85.31.62.223`

**📍 Registro 2 (Subdomínio www):**
- **Tipo:** A
- **Nome/Host:** `www`
- **Valor/Aponta para:** `85.31.62.223`

> ⏰ **Atenção:** As alterações de DNS podem levar de alguns minutos a algumas horas para se propagarem pela internet.

---

## Passo 2: Atualizar Configuração do Django

🐍 **Objetivo:** Configurar o Django para aceitar requisições do novo domínio.

### 2.1 Editar settings.py
Adicione seu novo domínio à lista `ALLOWED_HOSTS`:

```python
# settings.py
ALLOWED_HOSTS = [
    'sintonize.onrender.com', 
    '127.0.0.1',
    'localhost', 
    '85.31.62.223',
    'seunovodominio.com',        # ← Adicione seu domínio
    'www.seunovodominio.com'     # ← Adicione o subdomínio www
]
```

### 2.2 Atualizar na VPS
```bash
# Envie as alterações para o GitHub
git add .
git commit -m "Adicionar novo domínio ao ALLOWED_HOSTS"
git push origin main

# Na VPS, baixe as alterações
cd /root/sinto/Sintonize
git pull origin main
```

---

## Passo 3: Configurar Nginx

🌐 **Objetivo:** Configurar o servidor web para responder ao novo domínio.

### 3.1 Conectar via SSH e editar configuração
```bash
sudo nano /etc/nginx/sites-available/sintonize
```

### 3.2 Alterar server_name
Substitua o IP pelo seu novo domínio:

```nginx
server {
    listen 7080; 
    # Altere esta linha para seu domínio
    server_name seunovodominio.com www.seunovodominio.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

---

## Passo 4: Reiniciar os Serviços

🔄 **Aplicar todas as alterações:**

```bash
# Reinicia a aplicação Django
sudo systemctl restart gunicorn

# Reinicia o servidor web para carregar a nova configuração
sudo systemctl restart nginx
```

---

## ✅ Verificação

Após a propagação do DNS, seu site estará acessível em:
- `http://seunovodominio.com:7080`
- `http://www.seunovodominio.com:7080`

---

## 🔐 Próximo Passo: HTTPS (Essencial)

⚠️ **Importante:** Para um site em produção, você **deve** instalar um certificado SSL/TLS para:
- Ativar `https://`
- Proteger a comunicação dos usuários
- Remover avisos de "Não Seguro" dos navegadores

**Ferramenta recomendada:** Let's Encrypt com Certbot (gratuito)

