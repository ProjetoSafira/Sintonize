# 🚀 Guia de Deploy - Google Analytics Funcionando

## ⚠️ SITUAÇÃO ATUAL

- ✅ Fluxo do Google Analytics criado há 1 mês
- ❌ NENHUM dado foi coletado durante esse mês
- ✅ Código local está CORRETO e funcionando
- ❌ Código no servidor está COM PROBLEMA

## 📤 PASSO A PASSO PARA FAZER O DEPLOY

### **Passo 1: Verificar o Context Processor**

Certifique-se de que o arquivo `context_processors.py` está correto:

**Arquivo**: `Sintonize/site_sintonize/context_processors.py`

Deve conter:
```python
from django.conf import settings

def google_analytics(request):
    return {
        'GA_MEASUREMENT_ID': getattr(settings, 'GA_MEASUREMENT_ID', 'G-BRR6F0VRZ7'),
        'ENVIRONMENT': getattr(settings, 'ENVIRONMENT', 'development'),
        'DEBUG_MODE': getattr(settings, 'DEBUG', True),
    }
```

### **Passo 2: Verificar o Settings.py**

**Arquivo**: `Sintonize/setup/settings.py`

Certifique-se de que contém:
```python
# Google Analytics Configuration
GA_MEASUREMENT_ID = os.environ.get('GA_MEASUREMENT_ID', 'G-BRR6F0VRZ7')
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
```

E nos TEMPLATES:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'site_sintonize.context_processors.google_analytics',  # ← IMPORTANTE!
                'site_sintonize.context_processors.site_info',
            ],
        },
    },
]
```

### **Passo 3: Deploy para Hostinger**

**Opção A - Se usa Git:**
```bash
git add .
git commit -m "Fix: Google Analytics configurado corretamente"
git push origin main
```

**Opção B - Se usa FTP/Painel Hostinger:**
1. Acesse o painel da Hostinger
2. Vá em File Manager
3. Faça upload dos seguintes arquivos:
   - `site_sintonize/templates/base.html`
   - `site_sintonize/context_processors.py`
   - `setup/settings.py`

**Opção C - Se usa deploy automático:**
- Execute o comando de deploy que você normalmente usa

### **Passo 4: Reiniciar o Servidor Django**

Depois do upload, reinicie o servidor para aplicar as mudanças:

**No painel Hostinger:**
- Vá em "Advanced" → "Restart Server"
- Ou use SSH: `sudo systemctl restart [nome-do-serviço]`

### **Passo 5: TESTE IMEDIATO**

Após o deploy, faça o teste:

1. Acesse: `http://sintonize.online`
2. Abra o Console (F12)
3. Digite: `console.log(measurementId)`
4. **Resultado esperado**: `"G-BRR6F0VRZ7"`
5. Digite: `typeof gtag`
6. **Resultado esperado**: `"function"`

### **Passo 6: Verificar DebugView (Opcional)**

Se quiser ver os dados em tempo real para confirmar:

1. No arquivo `base.html`, **temporariamente** mude a linha 46:
   ```javascript
   config.debug_mode = true; // TESTE: debug ativado
   ```
2. Faça deploy novamente
3. Acesse Google Analytics → Admin → DebugView
4. Navegue no site
5. Veja os eventos aparecerem em tempo real
6. **DEPOIS**: volte para `debug_mode = false` e faça deploy novamente

---

## ✅ CHECKLIST PÓS-DEPLOY

- [ ] Arquivo `base.html` atualizado no servidor
- [ ] Arquivo `context_processors.py` atualizado no servidor
- [ ] Arquivo `settings.py` atualizado no servidor
- [ ] Servidor Django reiniciado
- [ ] Teste no console passou (measurementId = "G-BRR6F0VRZ7")
- [ ] Teste no console passou (typeof gtag = "function")
- [ ] Aguardar 24-48h para dados aparecerem nos relatórios

---

## 📊 QUANDO OS DADOS VÃO APARECER?

### **Tempo Real** (5-30 minutos)
- Local: Relatórios → Tempo Real → Visão Geral
- Mostra: Usuários ativos nos últimos 30 minutos

### **Relatórios Completos** (24-48 horas)
- Local: Relatórios → Resumo dos relatórios
- Mostra: Dados históricos, páginas mais visitadas, origem do tráfego, etc.

### **Dados Significativos** (7-14 dias)
- Para ter relatórios completos para enviar à equipe, aguarde pelo menos 1 semana de coleta

---

## 📧 COMO ENVIAR RELATÓRIOS PARA A EQUIPE

### **Opção 1: Relatório Manual (Imediato)**

1. Acesse: Relatórios → Resumo dos relatórios
2. Clique em "Compartilhar" (ícone no canto superior direito)
3. Escolha "Baixar PDF" ou "Baixar arquivo"
4. Envie por email para a equipe

### **Opção 2: Relatório Automático (Recomendado)**

1. No Google Analytics, vá em: **Biblioteca** (menu lateral esquerdo)
2. Clique em **Criar** → **Relatório**
3. Configure os dados que deseja mostrar
4. Clique em **Compartilhar** → **Agendar email**
5. Configure:
   - Emails dos destinatários (sua equipe)
   - Frequência: Diário, Semanal ou Mensal
   - Formato: PDF

### **Opção 3: Dashboard em Tempo Real (Avançado)**

Se você precisa de um dashboard que a equipe possa ver a qualquer momento:

1. **Google Analytics** → **Explorar** → **Criar nova exploração**
2. Configure os gráficos e métricas desejados
3. Clique em **Compartilhar** → **Compartilhar link**
4. Envie o link para a equipe (eles precisarão de acesso ao Google Analytics)

Ou crie um dashboard público usando o arquivo `analytics/dashboard.html` que já existe no projeto.

---

## 🆘 SE AINDA NÃO FUNCIONAR APÓS O DEPLOY

Se após fazer o deploy e aguardar 30 minutos os dados ainda não aparecerem:

1. **Verifique no Console**:
   ```javascript
   console.log(measurementId) // Deve ser "G-BRR6F0VRZ7"
   console.log(typeof gtag)   // Deve ser "function"
   console.log(window.dataLayer) // Deve ter dados
   ```

2. **Verifique erros no Console**:
   - Procure por erros em vermelho
   - Procure por avisos de CORS
   - Procure por bloqueios de conteúdo

3. **Verifique a rede**:
   - F12 → Aba Network
   - Filtre por "gtag" ou "analytics"
   - Veja se as requisições estão com status 200 ou 204

4. **Teste o arquivo de teste**:
   - Suba o arquivo `teste_analytics_simples.html` para o servidor
   - Acesse: `http://sintonize.online/teste_analytics_simples.html`
   - Clique nos botões de teste
   - Verifique se aparece no Google Analytics

---

## 📞 PRÓXIMOS PASSOS

1. **AGORA**: Fazer o deploy do código corrigido
2. **EM 30 MIN**: Verificar se os dados aparecem no Tempo Real
3. **EM 24-48H**: Verificar se os dados aparecem nos Relatórios
4. **EM 1 SEMANA**: Criar relatório semanal para enviar à equipe
5. **DEPOIS**: Configurar relatórios automáticos por email

---

**Data deste guia**: 2025-10-23
**Última atualização do código**: Hoje (debug_mode corrigido)
