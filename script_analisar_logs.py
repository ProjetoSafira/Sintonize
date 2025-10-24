"""
Script para Analisar Logs de Acesso do Servidor
Gera relatório detalhado de acessos de Outubro 2025

USO:
1. Baixe os logs de acesso da Hostinger
2. Coloque o arquivo na mesma pasta deste script
3. Execute: python script_analisar_logs.py nome_do_arquivo.log
"""

import re
from collections import defaultdict, Counter
from datetime import datetime
import sys

def analisar_logs(arquivo_log):
    """Analisa arquivo de logs e gera estatísticas"""

    print("🔍 Analisando logs de acesso...\n")

    acessos = []
    ips_unicos = set()
    paginas = Counter()
    user_agents = Counter()
    datas = Counter()
    horas = Counter()

    # Padrão típico de log Apache/Nginx
    # Exemplo: 192.168.1.1 - - [23/Oct/2025:10:30:45 +0000] "GET /index HTTP/1.1" 200 1234
    padrao = r'(\S+) .* \[(.*?)\] "(\w+) (.*?) HTTP.*?" (\d+) (\d+) "(.*?)" "(.*?)"'

    try:
        with open(arquivo_log, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                match = re.search(padrao, linha)
                if match:
                    ip = match.group(1)
                    timestamp = match.group(2)
                    metodo = match.group(3)
                    url = match.group(4)
                    status = match.group(5)
                    tamanho = match.group(6)
                    referer = match.group(7)
                    user_agent = match.group(8)

                    # Filtrar apenas acessos válidos (status 200-399)
                    if 200 <= int(status) < 400:
                        # Extrair data e hora
                        try:
                            dt = datetime.strptime(timestamp.split()[0], '%d/%b/%Y:%H:%M:%S')

                            # Filtrar apenas Outubro 2025
                            if dt.month == 10 and dt.year == 2025:
                                acessos.append({
                                    'ip': ip,
                                    'data': dt.date(),
                                    'hora': dt.hour,
                                    'url': url,
                                    'user_agent': user_agent,
                                    'status': status
                                })

                                ips_unicos.add(ip)
                                paginas[url] += 1
                                datas[dt.date()] += 1
                                horas[dt.hour] += 1

                                # Detectar tipo de dispositivo
                                if 'Mobile' in user_agent or 'Android' in user_agent or 'iPhone' in user_agent:
                                    user_agents['Mobile'] += 1
                                elif 'Bot' in user_agent or 'bot' in user_agent:
                                    user_agents['Bot'] += 1
                                else:
                                    user_agents['Desktop'] += 1
                        except ValueError:
                            continue

    except FileNotFoundError:
        print(f"❌ Arquivo '{arquivo_log}' não encontrado!")
        print("\nPara usar este script:")
        print("1. Baixe os logs de acesso da Hostinger")
        print("2. Coloque o arquivo na mesma pasta deste script")
        print("3. Execute: python script_analisar_logs.py nome_do_arquivo.log")
        return

    # Gerar relatório
    print("=" * 60)
    print("📊 RELATÓRIO DE ACESSOS - OUTUBRO 2025")
    print("=" * 60)
    print()

    print(f"📈 RESUMO GERAL")
    print(f"  Total de Acessos: {len(acessos)}")
    print(f"  Usuários Únicos (IPs): {len(ips_unicos)}")
    print(f"  Média de Acessos por Usuário: {len(acessos) / len(ips_unicos):.2f}" if ips_unicos else "N/A")
    print()

    print(f"📱 DISPOSITIVOS")
    for dispositivo, count in user_agents.most_common():
        percentual = (count / len(acessos) * 100) if acessos else 0
        print(f"  {dispositivo}: {count} ({percentual:.1f}%)")
    print()

    print(f"📄 TOP 10 PÁGINAS MAIS VISITADAS")
    for i, (url, count) in enumerate(paginas.most_common(10), 1):
        percentual = (count / len(acessos) * 100) if acessos else 0
        print(f"  {i}. {url}: {count} acessos ({percentual:.1f}%)")
    print()

    print(f"📅 ACESSOS POR DIA")
    for data in sorted(datas.keys()):
        count = datas[data]
        print(f"  {data.strftime('%d/%m/%Y')}: {count} acessos")
    print()

    print(f"🕐 HORÁRIOS DE PICO (Top 5)")
    for hora, count in horas.most_common(5):
        print(f"  {hora:02d}:00 - {hora+1:02d}:00: {count} acessos")
    print()

    print(f"🌐 TOP 5 IPs MAIS ATIVOS")
    ips_count = Counter([acesso['ip'] for acesso in acessos])
    for i, (ip, count) in enumerate(ips_count.most_common(5), 1):
        print(f"  {i}. {ip}: {count} acessos")
    print()

    # Salvar relatório em arquivo
    with open('relatorio_logs_outubro.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("📊 RELATÓRIO DE ACESSOS - SINTONIZE - OUTUBRO 2025\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"📈 RESUMO GERAL\n")
        f.write(f"  Total de Acessos: {len(acessos)}\n")
        f.write(f"  Usuários Únicos (IPs): {len(ips_unicos)}\n")
        f.write(f"  Média de Acessos por Usuário: {len(acessos) / len(ips_unicos):.2f}\n" if ips_unicos else "  N/A\n")
        f.write("\n")

        f.write(f"📱 DISPOSITIVOS\n")
        for dispositivo, count in user_agents.most_common():
            percentual = (count / len(acessos) * 100) if acessos else 0
            f.write(f"  {dispositivo}: {count} ({percentual:.1f}%)\n")
        f.write("\n")

        f.write(f"📄 TOP 10 PÁGINAS MAIS VISITADAS\n")
        for i, (url, count) in enumerate(paginas.most_common(10), 1):
            percentual = (count / len(acessos) * 100) if acessos else 0
            f.write(f"  {i}. {url}: {count} acessos ({percentual:.1f}%)\n")
        f.write("\n")

        f.write(f"📅 ACESSOS POR DIA\n")
        for data in sorted(datas.keys()):
            count = datas[data]
            f.write(f"  {data.strftime('%d/%m/%Y')}: {count} acessos\n")
        f.write("\n")

        f.write(f"🕐 HORÁRIOS DE PICO (Top 5)\n")
        for hora, count in horas.most_common(5):
            f.write(f"  {hora:02d}:00 - {hora+1:02d}:00: {count} acessos\n")
        f.write("\n")

    print("✅ Relatório salvo em: relatorio_logs_outubro.txt")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Uso: python script_analisar_logs.py arquivo_de_log.log")
        print("\nEXEMPLO:")
        print("  python script_analisar_logs.py access_log.txt")
        print("\n📌 Para obter os logs:")
        print("  1. Acesse: https://hpanel.hostinger.com/")
        print("  2. Vá em: Hosting → Seu site → Logs de Acesso")
        print("  3. Baixe os logs de Outubro 2025")
        print("  4. Execute este script com o arquivo baixado")
    else:
        arquivo = sys.argv[1]
        analisar_logs(arquivo)
