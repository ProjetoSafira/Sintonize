#!/bin/bash
# Script para gerar relatório de acessos de Outubro 2025
# Execute na VPS: bash gerar_relatorio_vps.sh

echo "🔍 Gerando Relatório de Acessos - Outubro 2025"
echo "=============================================="
echo ""

# Detectar qual servidor web está rodando
if [ -f /var/log/apache2/access.log ]; then
    LOG_FILE="/var/log/apache2/access.log"
elif [ -f /var/log/nginx/access.log ]; then
    LOG_FILE="/var/log/nginx/access.log"
elif [ -f /var/log/httpd/access_log ]; then
    LOG_FILE="/var/log/httpd/access_log"
else
    echo "❌ Arquivo de log não encontrado!"
    echo "Procure manualmente em:"
    echo "  - /var/log/apache2/"
    echo "  - /var/log/nginx/"
    echo "  - /var/log/httpd/"
    exit 1
fi

echo "✅ Log encontrado: $LOG_FILE"
echo ""

# Filtrar acessos de Outubro 2025
OUTUBRO_LOG=$(grep "Oct/2025" $LOG_FILE)

if [ -z "$OUTUBRO_LOG" ]; then
    echo "⚠️  Nenhum acesso encontrado em Outubro/2025"
    echo ""
    echo "Verificando últimos acessos:"
    tail -20 $LOG_FILE
    exit 0
fi

# Total de acessos
TOTAL_ACESSOS=$(echo "$OUTUBRO_LOG" | wc -l)
echo "📊 TOTAL DE ACESSOS EM OUTUBRO: $TOTAL_ACESSOS"
echo ""

# IPs únicos
IPS_UNICOS=$(echo "$OUTUBRO_LOG" | awk '{print $1}' | sort -u | wc -l)
echo "👥 USUÁRIOS ÚNICOS (IPs diferentes): $IPS_UNICOS"
echo ""

# Top 10 páginas mais acessadas
echo "📄 TOP 10 PÁGINAS MAIS VISITADAS:"
echo "$OUTUBRO_LOG" | awk '{print $7}' | grep -v "^\s*$" | sort | uniq -c | sort -rn | head -10 | nl
echo ""

# Top 5 IPs mais ativos
echo "🌐 TOP 5 IPs MAIS ATIVOS:"
echo "$OUTUBRO_LOG" | awk '{print $1}' | sort | uniq -c | sort -rn | head -5 | nl
echo ""

# Acessos por dia
echo "📅 ACESSOS POR DIA DE OUTUBRO:"
echo "$OUTUBRO_LOG" | awk '{print $4}' | cut -d: -f1 | cut -d/ -f1 | sort | uniq -c | awk '{printf "%s de Outubro: %s acessos\n", $2, $1}'
echo ""

# Horários de pico
echo "🕐 DISTRIBUIÇÃO POR HORA DO DIA (Top 10):"
echo "$OUTUBRO_LOG" | awk '{print $4}' | cut -d: -f2 | sort | uniq -c | sort -rn | head -10 | awk '{printf "%s:00h - %s acessos\n", $2, $1}'
echo ""

# Status codes
echo "📊 STATUS DAS REQUISIÇÕES:"
echo "$OUTUBRO_LOG" | awk '{print $9}' | sort | uniq -c | sort -rn | awk '{
    if ($2 == "200") status="✅ Sucesso";
    else if ($2 == "301" || $2 == "302") status="↗️  Redirecionamento";
    else if ($2 == "404") status="❌ Página não encontrada";
    else if ($2 == "500") status="⚠️  Erro no servidor";
    else status="Outros";
    printf "%s (%s): %s requisições\n", $2, status, $1
}'
echo ""

# Salvar relatório em arquivo
OUTPUT_FILE="/tmp/relatorio_sintonize_outubro_2025.txt"
{
    echo "=========================================="
    echo "RELATÓRIO DE ACESSOS - SINTONIZE"
    echo "Mês: Outubro 2025"
    echo "Data de Geração: $(date)"
    echo "=========================================="
    echo ""
    echo "📊 RESUMO:"
    echo "  Total de Acessos: $TOTAL_ACESSOS"
    echo "  Usuários Únicos: $IPS_UNICOS"
    echo "  Média de Acessos por Usuário: $(echo "scale=2; $TOTAL_ACESSOS / $IPS_UNICOS" | bc)"
    echo ""
    echo "📄 TOP 10 PÁGINAS:"
    echo "$OUTUBRO_LOG" | awk '{print $7}' | grep -v "^\s*$" | sort | uniq -c | sort -rn | head -10 | nl
    echo ""
    echo "🌐 TOP 5 IPs:"
    echo "$OUTUBRO_LOG" | awk '{print $1}' | sort | uniq -c | sort -rn | head -5 | nl
    echo ""
    echo "📅 ACESSOS POR DIA:"
    echo "$OUTUBRO_LOG" | awk '{print $4}' | cut -d: -f1 | cut -d/ -f1 | sort | uniq -c | awk '{printf "%s de Outubro: %s acessos\n", $2, $1}'
} > $OUTPUT_FILE

echo "✅ Relatório salvo em: $OUTPUT_FILE"
echo ""
echo "Para baixar o relatório para seu computador, execute:"
echo "  scp seu_usuario@$(hostname -I | awk '{print $1}'):$OUTPUT_FILE ."
echo ""
echo "Ou visualize agora com:"
echo "  cat $OUTPUT_FILE"
