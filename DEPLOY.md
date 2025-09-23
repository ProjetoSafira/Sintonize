# Deploy Sintonize com Docker + Traefik

## Pré-requisitos
- Traefik rodando na VPS com rede `traefik_default`
- Portainer configurado (opcional, mas recomendado)
- Projeto já clonado na VPS: `/root/sinto/Sintonize`

## Passos para Deploy

### 1. Atualizar código na VPS via Git
```bash
# No computador local, commit e push das alterações
git add .
git commit -m "Update Docker configuration"
git push origin main

# Na VPS, fazer pull das atualizações
cd /root/sinto/Sintonize
git pull origin main

# Verificar se arquivos Docker foram baixados
ls -la | grep -E "(Dockerfile|docker-compose)"
```

### 2. Parar serviço Gunicorn atual
```bash
# Parar processos Gunicorn existentes
sudo pkill -f gunicorn

# Verificar se pararam
ps aux | grep gunicorn

# Desabilitar configuração Nginx atual (opcional)
sudo rm /etc/nginx/sites-enabled/sintonize
sudo systemctl reload nginx
```

### 3. Deploy via Docker

#### Opção A: Via Portainer (Interface Gráfica)
1. Acesse Portainer: `http://85.31.62.223:9000`
2. Vá em **Stacks** → **Add Stack**
3. Nome: `sintonize`
4. Cole o conteúdo do `docker-compose.yml`
5. **Deploy the stack**

#### Opção B: Via Terminal
```bash
cd /root/sinto/Sintonize
docker-compose up -d --build
```

### 4. Verificar Deploy
```bash
# Ver containers rodando
docker ps | grep sintonize

# Ver logs da aplicação
docker logs sintonize_app

# Ver logs do Traefik
docker logs traefik_traefik.1.bd94hsefc9ri8lsbkg8ikab2l

# Testar localmente
curl -H "Host: sintonize.online" http://localhost

# Testar diretamente o container
docker exec -it sintonize_app curl http://localhost:8000
```

### 5. Testar no navegador
- Acesse: `http://sintonize.online`
- Deve redirecionar automaticamente para: `https://sintonize.online`

## Configuração do Traefik

O Traefik irá automaticamente:
- Detectar o container via labels
- Rotear `sintonize.online` para o container
- Gerar certificado SSL via Let's Encrypt
- Redirecionar HTTP → HTTPS

## Troubleshooting

### Container não inicia
```bash
docker logs sintonize_app
```

### Domínio não resolve
```bash
# Verificar se Traefik detectou o serviço
docker logs traefik_traefik.1.bd94hsefc9ri8lsbkg8ikab2l
```

### SSL não funciona
- Aguardar propagação DNS (até 24h)
- Verificar se cert resolver está configurado no Traefik

## Atualizações Futuras

Para atualizar a aplicação:
```bash
# 1. No computador local, fazer commit e push
git add .
git commit -m "Nova atualização"
git push origin main

# 2. Na VPS, atualizar e redeployar
cd /root/sinto/Sintonize
git pull origin main
docker-compose down
docker-compose up -d --build

# 3. Verificar
docker ps | grep sintonize
```

## Caminho Completo na VPS
- **Projeto**: `/root/sinto/Sintonize`
- **Aplicação atual**: Gunicorn rodando via systemd
- **Nova aplicação**: Container Docker integrado com Traefik