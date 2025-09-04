# 📊 Rastreamento do Formulário de Sondagem - Google Analytics

## 🎯 Visão Geral

Este documento descreve a implementação completa do rastreamento do formulário de sondagem de burnout no Google Analytics 4 (GA4), permitindo monitorar o funil de preenchimento detalhadamente.

## 🚀 Funcionalidades Implementadas

### 1. Rastreamento de Visualização das Perguntas

**Como funciona:**
- Cada uma das 12 perguntas é rastreada individualmente quando se torna visível para o usuário
- Utiliza dupla estratégia de rastreamento:
  - **Navegação por botões**: Detecta quando o usuário navega entre perguntas usando os botões "Próximo" e "Voltar"
  - **Intersection Observer API**: Detecta quando perguntas entram na área de visualização (útil para navegação rápida)

**Eventos enviados:**
- **Action**: `question_view`
- **Category**: `Formulário de Sondagem`
- **Label**: `Pergunta 1`, `Pergunta 2`, ..., `Pergunta 12`
- **Value**: Número da pergunta (1-12)

### 2. Rastreamento de Conclusão do Formulário

**Como funciona:**
- Dispara um evento quando o usuário clica no botão "Enviar" após responder todas as perguntas

**Evento enviado:**
- **Action**: `form_completion`
- **Category**: `Formulário de Sondagem`
- **Label**: `Formulário Concluído`
- **Value**: 1

### 3. Rastreamento da Pontuação do Formulário

**Como funciona:**
- Dispara um evento após o processamento bem-sucedido do formulário no backend
- Envia a pontuação final calculada como valor do evento
- Garante que apenas resultados válidos sejam rastreados

**Evento enviado:**
- **Action**: `survey_score`
- **Category**: `Formulário de Sondagem`
- **Label**: `Resultado do Teste`
- **Value**: Pontuação final (12-60)

## 📈 Como Monitorar no Google Analytics

### 1. Acessar os Eventos no GA4

1. **Acesse o Google Analytics**: https://analytics.google.com
2. **Navegue para**: Relatórios > Engajamento > Eventos
3. **Filtrar por categoria**: `Formulário de Sondagem`

### 2. Criar Relatórios Personalizados

#### A. Funil de Preenchimento por Pergunta

```
Dimensão Primária: Event Label
Métrica: Event Count
Filtro: Event Category = "Formulário de Sondagem"
```

**Resultado esperado:**
- Pergunta 1: [X] eventos
- Pergunta 2: [Y] eventos  
- Pergunta 3: [Z] eventos
- ...
- Pergunta 12: [W] eventos
- Formulário Concluído: [V] eventos
- Resultado do Teste: [V] eventos (com pontuações como valores)

#### B. Taxa de Abandono por Pergunta

Para calcular em qual pergunta os usuários mais desistem:

```
Taxa de Abandono = (Visualizações Pergunta N - Visualizações Pergunta N+1) / Visualizações Pergunta N * 100
```

#### C. Análise de Pontuações dos Usuários

Para analisar o desempenho e padrões nos resultados:

```
Dimensão Primária: Event Label (filtrar por "Resultado do Teste")
Métrica: Event Value (pontuação)
Métricas adicionais: Event Count, Average Event Value
Filtro: Event Category = "Formulário de Sondagem" AND Event Label = "Resultado do Teste"
```

**Métricas relevantes:**
- **Pontuação média**: Average Event Value
- **Distribuição de pontuações**: Gráfico de Event Value
- **Total de testes concluídos**: Event Count
- **Faixas de risco**:
  - Baixo risco: 12-20 pontos
  - Cuidado: 21-30 pontos  
  - Alerta: 31-40 pontos
  - Alto risco: 41-50 pontos
  - Crítico: 51-60 pontos

### 3. Configurar Conversões

Para acompanhar a conclusão do formulário como conversão:

1. **Vá para**: Configurar > Eventos > Criar Eventos
2. **Crie um evento personalizado**:
   - Nome: `formulario_sondagem_concluido`
   - Condições: `event_name = form_completion AND event_category = Formulário de Sondagem`
3. **Marque como conversão**

### 4. Dashboards Recomendados

#### Dashboard: Análise do Formulário de Sondagem

**Cartões sugeridos:**

1. **Total de Iniciados**: Count de "Pergunta 1"
2. **Total de Concluídos**: Count de "Formulário Concluído"
3. **Taxa de Conclusão**: (Concluídos / Iniciados) * 100
4. **Gráfico de Funil**: Visualizações por pergunta (1-12)
5. **Principais Pontos de Abandono**: Perguntas com maior queda

## 🔧 Configuração Técnica

### Arquivos Modificados

1. **`base.html`**: Funções de tracking global
   - `trackSurveyQuestionView(questionNumber)`
   - `trackSurveyFormCompletion()`

2. **`burnout_survey.html`**: Implementação do rastreamento
   - Intersection Observer API
   - Tracking na navegação por botões
   - Tracking na conclusão do formulário

### Otimizações de Performance

- **Rastreamento único**: Cada pergunta é rastreada apenas uma vez, mesmo se visualizada múltiplas vezes
- **Intersection Observer**: Usa API nativa do browser para detecção eficiente de visibilidade
- **Fallback graceful**: Funciona mesmo se o Google Analytics não estiver carregado
- **Não-bloqueante**: Todo o rastreamento é assíncrono e não afeta a UX

## 📊 Métricas Importantes para Acompanhar

### 1. Métricas de Funil

- **Taxa de Início**: Usuários que visualizaram a Pergunta 1
- **Taxa de Conclusão Geral**: (Formulários Concluídos / Pergunta 1) * 100
- **Taxa de Abandono por Seção**:
  - Seção 1 (Perguntas 1-4)
  - Seção 2 (Perguntas 5-8)  
  - Seção 3 (Perguntas 9-12)

### 2. Análise de Pontos Críticos

- **Pergunta com maior abandono**: Identifique onde mais usuários param
- **Tempo médio por pergunta**: Use eventos customizados se necessário
- **Padrões por dispositivo**: Desktop vs Mobile vs Tablet

### 3. Segmentação Recomendada

- **Por fonte de tráfego**: Orgânico, direto, redes sociais
- **Por dispositivo**: Desktop, mobile, tablet
- **Por horário**: Identifique melhores momentos para engajamento
- **Por localização**: Diferentes regiões podem ter comportamentos distintos

## 🎯 Objetivos de Negócio Atendidos

✅ **Identificar total de usuários que iniciaram o formulário**
- Métrica: Count de "Pergunta 1"

✅ **Monitorar visualização de cada pergunta**
- Métrica: Count individual de "Pergunta X" (1-12)

✅ **Rastrear conclusões do formulário**
- Métrica: Count de "Formulário Concluído"

✅ **Identificar pontos de abandono**
- Análise: Comparação entre perguntas sequenciais

✅ **Performance otimizada**
- Implementação não-bloqueante e eficiente

## 🚨 Monitoramento e Alertas

### Alertas Recomendados

1. **Queda na Taxa de Conclusão**: Se taxa de conclusão cair abaixo de X%
2. **Aumento no Abandono**: Se abandono em pergunta específica aumentar significativamente
3. **Problemas Técnicos**: Se eventos param de ser enviados

### Verificação da Implementação

Use o **Google Analytics DebugView** para verificar se os eventos estão sendo enviados corretamente:

1. Ative o modo de depuração: `gtag('config', 'GA_MEASUREMENT_ID', { debug_mode: true })`
2. Acesse: Google Analytics > Configurar > DebugView
3. Teste o formulário e verifique se os eventos aparecem em tempo real

## 📞 Suporte

Para dúvidas sobre a implementação ou análise dos dados, consulte:
- Documentação do Google Analytics 4
- Este arquivo de documentação
- Logs do console do navegador para debug
