# 🧪 Comandos para Testar o Sistema de Monitoramento

## 🚀 Inicialização e Configuração

### 1. Executar Migrações
```bash
cd Sintonize
python manage.py makemigrations
python manage.py migrate
```

### 2. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 3. Coletar Arquivos Estáticos
```bash
python manage.py collectstatic --noinput
```

### 4. Iniciar Servidor de Desenvolvimento
```bash
python manage.py runserver
```

## 🔗 URLs para Testar

### Páginas Principais
- **Página Inicial:** http://127.0.0.1:8000/
- **Sondagem de Burnout:** http://127.0.0.1:8000/sondagem.html
- **Painel de Monitoramento:** http://127.0.0.1:8000/analytics/
- **API de Dados:** http://127.0.0.1:8000/analytics/api/

### Exportação de Dados
- **CSV Semana:** http://127.0.0.1:8000/analytics/export/?periodo=week&formato=csv
- **JSON Mês:** http://127.0.0.1:8000/analytics/export/?periodo=month&formato=json
- **CSV Hoje:** http://127.0.0.1:8000/analytics/export/?periodo=day&formato=csv

## 🧪 Testes Funcionais

### 1. Testar Rastreamento Básico
```bash
# Simular visitas às páginas
curl -s http://127.0.0.1:8000/ > /dev/null
curl -s http://127.0.0.1:8000/sondagem.html > /dev/null
curl -s http://127.0.0.1:8000/trilha/ > /dev/null
```

### 2. Testar API de Dados
```bash
# Testar API com diferentes períodos
curl -s http://127.0.0.1:8000/analytics/api/?periodo=day | python -m json.tool
curl -s http://127.0.0.1:8000/analytics/api/?periodo=week | python -m json.tool
curl -s http://127.0.0.1:8000/analytics/api/?periodo=month | python -m json.tool
```

### 3. Testar Exportação
```bash
# Baixar relatórios de teste
curl -o relatorio_week.csv "http://127.0.0.1:8000/analytics/export/?periodo=week&formato=csv"
curl -o relatorio_month.json "http://127.0.0.1:8000/analytics/export/?periodo=month&formato=json"
```

## 📊 Validação do Google Analytics

### 1. Verificar Código no HTML
```bash
# Verificar se o código do GA está presente
curl -s http://127.0.0.1:8000/ | grep -i "gtag\|analytics"
```

### 2. Verificar Eventos Personalizados
```bash
# Verificar se funções estão definidas
curl -s http://127.0.0.1:8000/ | grep -i "trackEvent\|trackBurnoutSurvey"
```

## 🔍 Testes de Integração

### 1. Testar com Diferentes User-Agents
```bash
# Simular diferentes dispositivos
curl -s -A "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)" http://127.0.0.1:8000/
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" http://127.0.0.1:8000/
curl -s -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" http://127.0.0.1:8000/
```

### 2. Testar com Referrers
```bash
# Simular tráfego de diferentes origens
curl -s -H "Referer: https://google.com" http://127.0.0.1:8000/
curl -s -H "Referer: https://facebook.com" http://127.0.0.1:8000/
curl -s -H "Referer: https://instagram.com" http://127.0.0.1:8000/
```

## 🐛 Testes de Debugging

### 1. Verificar Logs do Django
```bash
# Executar com logs detalhados
python manage.py runserver --verbosity=2
```

### 2. Testar URLs Protegidas
```bash
# Testar acesso sem autenticação (deve dar erro 302/403)
curl -w "%{http_code}" -s -o /dev/null http://127.0.0.1:8000/analytics/
```

### 3. Testar Parâmetros Inválidos
```bash
# API com parâmetros inválidos
curl -s "http://127.0.0.1:8000/analytics/api/?periodo=invalid" | python -m json.tool
curl -s "http://127.0.0.1:8000/analytics/export/?periodo=invalid&formato=invalid"
```

## 🎯 Testes de Performance

### 1. Testar Múltiplas Requisições
```bash
# Simular múltiplos acessos simultâneos
for i in {1..10}; do
    curl -s http://127.0.0.1:8000/ > /dev/null &
done
wait
```

### 2. Testar Carga na API
```bash
# Testar API com múltiplas requisições
for i in {1..5}; do
    curl -s "http://127.0.0.1:8000/analytics/api/?periodo=week" > /dev/null &
done
wait
```

## 🌐 Testes de Produção

### 1. Verificar HTTPS (em produção)
```bash
# Verificar se o Google Analytics funciona com HTTPS
curl -s https://seusite.com/ | grep -i "gtag"
```

### 2. Testar Compress/Gzip
```bash
# Verificar compressão de arquivos estáticos
curl -H "Accept-Encoding: gzip" -s https://seusite.com/static/css/styles.css | head -1
```

## 🔧 Comandos de Manutenção

### 1. Limpar Cache
```bash
# Limpar cache do Django
python manage.py clearsessions
```

### 2. Verificar Configuração
```bash
# Verificar configurações do Django
python manage.py check --deploy
```

### 3. Coletar Estatísticas
```bash
# Comando personalizado para gerar estatísticas (se implementado)
python manage.py collectstats
```

## 📋 Checklist de Testes

### ✅ Funcionalidades Básicas
- [ ] Página inicial carrega corretamente
- [ ] Código do Google Analytics está presente
- [ ] Painel de analytics é acessível (com login)
- [ ] API retorna dados em JSON
- [ ] Exportação CSV funciona
- [ ] Exportação JSON funciona

### ✅ Rastreamento
- [ ] Eventos personalizados são chamados
- [ ] Diferentes páginas são rastreadas
- [ ] Botão de sondagem tem rastreamento
- [ ] Tempo na página é medido

### ✅ Segurança
- [ ] Painel requer autenticação
- [ ] Dados sensíveis não são expostos
- [ ] URLs protegidas retornam 403/302
- [ ] Parâmetros inválidos são tratados

### ✅ Performance
- [ ] Páginas carregam rapidamente
- [ ] API responde em tempo adequado
- [ ] Exportação não trava o servidor
- [ ] Múltiplas requisições são suportadas

## 🚨 Problemas Comuns e Soluções

### Problema: Painel não carrega
**Solução:**
```bash
# Verificar se superusuário existe
python manage.py createsuperuser

# Verificar URLs
python manage.py show_urls | grep analytics
```

### Problema: API retorna erro 500
**Solução:**
```bash
# Verificar logs detalhados
python manage.py runserver --verbosity=2

# Verificar configuração
python manage.py check
```

### Problema: Exportação falha
**Solução:**
```bash
# Verificar permissões de arquivo
ls -la /tmp/

# Testar com dados diferentes
curl -s "http://127.0.0.1:8000/analytics/export/?periodo=day&formato=csv"
```

## 📊 Exemplo de Resultado Esperado

### API Response (analytics/api/):
```json
{
  "visitantes_hoje": 0,
  "visitantes_semana": 0,
  "visitantes_mes": 0,
  "paginas_populares": [
    {
      "pagina": "/",
      "titulo": "Página Inicial",
      "visualizacoes": 0
    }
  ],
  "fontes_trafego": [
    {
      "fonte": "Direto",
      "visitantes": 0,
      "percentual": 0
    }
  ],
  "dispositivos": {
    "desktop": 0,
    "mobile": 0,
    "tablet": 0
  }
}
```

## 🎯 Próximos Passos Após Testes

1. **Configurar Google Analytics real** (substituir GA_MEASUREMENT_ID)
2. **Aguardar 24-48 horas** para dados aparecerem
3. **Testar com tráfego real** do site
4. **Configurar relatórios automáticos**
5. **Treinar equipe** no uso da ferramenta

---

**Nota:** Lembre-se de configurar o Google Analytics real para ver dados reais. Os testes acima mostram a estrutura funcionando, mas os dados só aparecerão após configuração completa do GA4. 