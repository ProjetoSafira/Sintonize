# 🔧 Configuração Google Analytics - Apenas VPN Hostinger

## 📋 Configurações Necessárias no Google Analytics

Agora que o código está configurado para enviar dados apenas da VPN Hostinger, você precisa ajustar as configurações no painel do Google Analytics.

## 🚀 Passo a Passo:

### 1. Acesso ao Google Analytics

1. **Acesse:** https://analytics.google.com
2. **Faça login** com sua conta Google
3. **Selecione a propriedade:** Sintonize (ID: G-BRR6F0VRZ7)

### 2. Configurar Domínio da VPN Hostinger

#### 2.1 Fluxos de Dados
1. **Navegue para:** Admin (⚙️) > Fluxos de dados
2. **Clique no fluxo** existente ou crie um novo
3. **Configure:**
   - **URL do site:** `http://85.31.62.223:7080`
   - **Nome do fluxo:** "Sintonize VPN Hostinger"

#### 2.2 Configurações Avançadas
1. **No fluxo de dados**, clique em **"Configurações avançadas"**
2. **Lista de referenciadores excluídos:**
   - Adicione: `sintonize.onrender.com` (para ignorar tráfego do Render)
3. **Domínios confiáveis:**
   - Adicione: `85.31.62.223`

### 3. Filtros de Dados

#### 3.1 Criar Filtro para Apenas VPN Hostinger
1. **Admin** > **Filtros de dados**
2. **Criar filtro** com as seguintes configurações:

```
Nome do filtro: Apenas VPN Hostinger
Tipo de filtro: Incluir
Campo: Hostname
Condição: Igual a
Valor: 85.31.62.223
```

#### 3.2 Filtro para Excluir Render (opcional)
```
Nome do filtro: Excluir Render
Tipo de filtro: Excluir
Campo: Hostname
Condição: Contém
Valor: onrender.com
```

### 4. Configurar Eventos Personalizados

#### 4.1 Verificar Eventos Existentes
1. **Configurar** > **Eventos**
2. **Verificar se existem:**
   - `question_view`
   - `form_completion`
   - `survey_score`

#### 4.2 Marcar Eventos como Conversões
1. **Clique no evento** `form_completion`
2. **Ative a opção** "Marcar como conversão"
3. **Faça o mesmo para** `survey_score`

### 5. Configurar Audiências

#### 5.1 Criar Audiência "Usuários VPN Hostinger"
1. **Configurar** > **Audiências** > **Nova audiência**
2. **Nome:** "Usuários VPN Hostinger"
3. **Condições:**
   ```
   Hostname = 85.31.62.223
   ```

#### 5.2 Criar Audiência "Completaram Formulário"
1. **Nome:** "Completaram Formulário de Sondagem"
2. **Condições:**
   ```
   Evento = form_completion
   E
   Hostname = 85.31.62.223
   ```

### 6. Configurar Relatórios Personalizados

#### 6.1 Biblioteca de Relatórios
1. **Relatórios** > **Biblioteca**
2. **Criar relatório personalizado:**

**Nome:** Análise Formulário Sondagem VPN
**Métricas:**
- Total de usuários
- Eventos (question_view)
- Eventos (form_completion)
- Eventos (survey_score)

**Dimensões:**
- Hostname
- Event name
- Event label

**Filtros:**
- Hostname = 85.31.62.223

### 7. Configurar Alertas

#### 7.1 Alertas Personalizados
1. **Admin** > **Alertas personalizados**
2. **Criar alerta:**

```
Nome: Queda no Tráfego VPN
Condição: Usuários diários < 5
Período: Diário
Aplicar a: Hostname = 85.31.62.223
```

### 8. Configurações de Dados

#### 8.1 Retenção de Dados
1. **Admin** > **Configurações de dados** > **Retenção de dados**
2. **Configurar para:** 26 meses (máximo)

#### 8.2 Exclusão de Tráfego de Bots
1. **Configurações de dados** > **Filtros de dados**
2. **Ativar:** "Excluir todos os hits de bots e aranhas conhecidos"

### 9. Verificar Propriedade

#### 9.1 Verificação do Site
1. **Admin** > **Informações da propriedade**
2. **Verificar se está configurado:**
   - **URL da propriedade:** `http://85.31.62.223:7080`
   - **Fuso horário:** America/Sao_Paulo
   - **Moeda:** Real brasileiro (BRL)

### 10. Teste de Configuração

#### 10.1 Relatórios em Tempo Real
1. **Relatórios** > **Tempo real** > **Visão geral**
2. **Acesse:** `http://85.31.62.223:7080`
3. **Navegue pelo site** e verifique se aparece em tempo real
4. **Teste o formulário** de sondagem

#### 10.2 Verificar Eventos
1. **Tempo real** > **Eventos**
2. **Procure por:**
   - `question_view`
   - `form_completion`
   - `survey_score`

## ✅ Checklist de Configuração:

- [ ] Fluxo de dados configurado para VPN Hostinger
- [ ] Filtros criados (incluir VPN, excluir Render)
- [ ] Eventos personalizados verificados
- [ ] Conversões marcadas (form_completion, survey_score)
- [ ] Audiências criadas
- [ ] Relatórios personalizados configurados
- [ ] Alertas configurados
- [ ] Teste em tempo real realizado
- [ ] Formulário de sondagem testado

## 🔍 Verificação Final:

### URLs para Teste:
- ✅ **COM GA:** `http://85.31.62.223:7080`
- ❌ **SEM GA:** `https://sintonize.onrender.com`

### Dados que Devem Aparecer no GA:
1. **Page views** apenas de `85.31.62.223`
2. **Eventos do formulário** de sondagem
3. **Nenhum tráfego** de `onrender.com`

### Console do Navegador (F12):
- **Na VPN:** `Google Analytics ativo: true`
- **No Render:** `Google Analytics ativo: false`

## 🆘 Problemas Comuns:

### Não aparece tráfego em tempo real:
1. Verificar se está acessando `http://85.31.62.223:7080`
2. Limpar cache do navegador
3. Desativar bloqueadores de anúncios
4. Aguardar alguns minutos

### Eventos não aparecem:
1. Testar o formulário de sondagem
2. Verificar console do navegador
3. Verificar se eventos estão sendo enviados
4. Aguardar até 24h para relatórios completos

### Ainda recebe dados do Render:
1. Verificar se filtros estão ativos
2. Aguardar processamento (pode levar horas)
3. Verificar se código foi atualizado na VPS

## 📞 Links Úteis:

- **Google Analytics:** https://analytics.google.com
- **ID da Propriedade:** G-BRR6F0VRZ7
- **Documentação GA4:** https://developers.google.com/analytics/devguides/collection/ga4
- **Debug View:** https://analytics.google.com/analytics/web/#/a495597072p495597072/debugview

---

**🎯 OBJETIVO:** Configurar o Google Analytics para receber dados apenas da VPN Hostinger (`85.31.62.223:7080`) e ignorar completamente o tráfego do Render (`sintonize.onrender.com`).


