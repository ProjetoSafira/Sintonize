# 📊 Guia de Monitoramento do Site Sintonize

## 🎯 Visão Geral

Este sistema de monitoramento oferece análise completa dos acessos ao site Sintonize usando Google Analytics 4 (GA4). Ele atende todos os critérios de aceitação solicitados:

- ✅ Contabiliza cada novo acesso ao site
- ✅ Visualização de dados por período (dia, semana, mês)
- ✅ Registro da origem dos acessos
- ✅ Painel visual e funcionalidade de exportação

## 🛠️ Configuração Inicial

### 1. Configurar Google Analytics

1. **Acesse o Google Analytics:**
   - Visite: https://analytics.google.com
   - Faça login com sua conta Google

2. **Crie uma propriedade:**
   - Clique em "Começar"
   - Crie uma conta (se não tiver)
   - Adicione uma propriedade para o site Sintonize
   - Escolha "Web" como plataforma

3. **Obtenha o ID de Medição:**
   - Após criar a propriedade, você receberá um ID no formato: `G-XXXXXXXXXX`
   - Copie este ID

4. **Configure no código:**
   - Abra o arquivo: `Sintonize/site_sintonize/templates/base.html`
   - Procure por: `GA_MEASUREMENT_ID`
   - Substitua ambas as ocorrências pelo seu ID real

   ```html
   <!-- Altere esta linha -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   
   <!-- E esta linha -->
   gtag('config', 'G-XXXXXXXXXX', {
   ```

### 2. Executar Migrações (Opcional)

Se você quiser usar o sistema de backup interno também:

```bash
cd Sintonize
python manage.py makemigrations
python manage.py migrate
```

### 3. Criar Superusuário

Para acessar o painel de monitoramento:

```bash
python manage.py createsuperuser
```

## 📈 Funcionalidades Implementadas

### 1. Rastreamento Automático

**O que é monitorado:**
- Todas as páginas do site
- Origem dos visitantes (referrer)
- Tipo de dispositivo (desktop, mobile, tablet)
- Navegador e sistema operacional
- Tempo gasto em cada página
- Eventos especiais (cliques em botões importantes)

**O que NÃO é monitorado:**
- Arquivos estáticos (CSS, JS, imagens)
- Páginas de admin
- Bots e crawlers
- Arquivos de sistema (robots.txt, favicon)

### 2. Painel de Monitoramento

**Acesso:** http://seusite.com/analytics/

**Funcionalidades:**
- 📊 Estatísticas em tempo real
- 📈 Gráficos interativos
- 📋 Tabelas de dados
- 🔄 Atualização automática
- 📱 Interface responsiva

### 3. Exportação de Dados

**Formatos disponíveis:**
- **CSV:** Ideal para Excel e análise em planilhas
- **JSON:** Para desenvolvedores e integração com outras ferramentas

**Períodos disponíveis:**
- Hoje
- Última semana
- Último mês

## 🚀 Como Usar

### 1. Monitoramento Básico

Depois de configurar o Google Analytics:

1. **Aguarde 24-48 horas** para os primeiros dados aparecerem
2. Acesse o painel: `/analytics/`
3. Faça login com sua conta de admin
4. Visualize as estatísticas em tempo real

### 2. Visualizar Dados por Período

No painel de monitoramento:

1. Selecione o período desejado (dia, semana, mês)
2. Clique em "Atualizar"
3. Os dados serão carregados automaticamente

### 3. Exportar Relatórios

1. Escolha o período desejado
2. Clique em "Exportar CSV" ou "Exportar JSON"
3. O arquivo será baixado automaticamente

### 4. Monitorar Origem dos Acessos

O sistema registra automaticamente:
- **Tráfego direto:** Visitantes que digitaram a URL
- **Tráfego do Google:** Vindos de pesquisas
- **Redes sociais:** Facebook, Instagram, etc.
- **Sites de referência:** Outros sites que linkaram para o seu

## 📊 Eventos Personalizados

### Eventos Já Configurados:

1. **Clique na Sondagem de Burnout:**
   - Categoria: engagement
   - Ação: click
   - Label: burnout_survey_start

2. **Tempo na Página:**
   - Categoria: timing_complete
   - Nome: page_view_time

3. **Downloads:**
   - Categoria: file
   - Ação: download

### Adicionar Novos Eventos:

Para rastrear outros eventos, use a função `trackEvent()`:

```javascript
// Exemplo: Rastrear clique em um botão
<button onclick="trackEvent('click', 'button', 'nome_do_botao', 1)">
    Meu Botão
</button>
```

## 🔐 Segurança e Privacidade

### Dados Coletados:
- Endereço IP (anonimizado pelo Google)
- Páginas visitadas
- Tipo de dispositivo
- Navegador
- Referrer (site de origem)

### Dados NÃO Coletados:
- Informações pessoais
- Senhas
- Dados sensíveis
- Cookies desnecessários

### Conformidade LGPD:
- Todos os dados são processados pelo Google Analytics
- Não armazenamos dados pessoais em nosso servidor
- Os dados são anonimizados

## 🔧 Troubleshooting

### Problema: Dados não aparecem

**Soluções:**
1. Verifique se o ID do Google Analytics está correto
2. Aguarde 24-48 horas após a configuração
3. Verifique se o site está recebendo visitas
4. Teste em uma aba anônima do navegador

### Problema: Painel não carrega

**Soluções:**
1. Verifique se está logado como superusuário
2. Confirme se as URLs estão configuradas corretamente
3. Verifique os logs do Django para erros

### Problema: Exportação não funciona

**Soluções:**
1. Verifique se há dados para o período selecionado
2. Teste com períodos diferentes
3. Verifique as permissões de usuário

## 📋 Relatórios Disponíveis

### 1. Relatório de Visitantes
- Total de visitantes por período
- Visitantes únicos
- Usuários ativos em tempo real

### 2. Relatório de Páginas
- Páginas mais visitadas
- Tempo médio em cada página
- Taxa de rejeição

### 3. Relatório de Tráfego
- Origens de tráfego
- Referrers mais comuns
- Canais de marketing

### 4. Relatório de Tecnologia
- Dispositivos mais usados
- Navegadores populares
- Sistemas operacionais

## 🎯 Próximos Passos

### Integrações Avançadas:

1. **Google Analytics Reporting API:**
   - Dados mais detalhados
   - Relatórios personalizados

2. **Google Tag Manager:**
   - Gestão avançada de tags
   - Eventos mais complexos

3. **Google Data Studio:**
   - Dashboards profissionais
   - Relatórios avançados

### Melhorias Futuras:

1. **Alertas automáticos** para picos de tráfego
2. **Integração com email** para relatórios periódicos
3. **API própria** para dados customizados
4. **Comparação** de períodos

## 📞 Suporte

Para dúvidas ou problemas:

1. **Documentação do Google Analytics:** https://support.google.com/analytics
2. **Documentação do Django:** https://docs.djangoproject.com
3. **Logs do sistema:** Verifique os logs do Django para erros específicos

## 🎉 Conclusão

Este sistema de monitoramento oferece uma solução completa e profissional para analisar o desempenho do site Sintonize. Com o Google Analytics integrado, você terá acesso a:

- ✅ Dados precisos e confiáveis
- ✅ Interface profissional
- ✅ Relatórios detalhados
- ✅ Funcionalidade de exportação
- ✅ Monitoramento em tempo real

O sistema está pronto para uso e pode ser expandido conforme suas necessidades crescerem!

---

**Versão:** 1.0  
**Última atualização:** Janeiro 2025  
**Compatibilidade:** Django 5.x, Google Analytics 4 