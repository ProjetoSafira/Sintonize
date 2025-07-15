#!/usr/bin/env python3
"""
Script para testar diferentes IDs do Google Analytics
"""
import requests
import time
from datetime import datetime

# IDs para testar
GA_IDS_TESTE = [
    "G-BRR6F0VRZ7",  # ID atual
    "G-XXXXXXXXXX",  # Substitua pelo seu ID real
    "UA-XXXXXXXXX-1", # Formato antigo (Universal Analytics)
]

SITE_URL = "http://127.0.0.1:8000"

def testar_id_ga(ga_id):
    """Testa se um ID do Google Analytics está funcionando"""
    print(f"\n🧪 TESTANDO ID: {ga_id}")
    print("-" * 40)
    
    try:
        # Verificar se o site está rodando
        response = requests.get(SITE_URL, timeout=5)
        if response.status_code != 200:
            print("❌ Site não está rodando!")
            return False
        
        # Verificar se o ID está no código
        content = response.text
        if ga_id in content:
            print("✅ ID encontrado no código HTML")
            
            # Verificar se o script do GA está sendo carregado
            ga_script_url = f"https://www.googletagmanager.com/gtag/js?id={ga_id}"
            if ga_script_url in content:
                print("✅ Script do GA está sendo carregado")
                
                # Tentar fazer requisição para o script do GA
                try:
                    ga_response = requests.get(ga_script_url, timeout=5)
                    if ga_response.status_code == 200:
                        print("✅ Script do GA respondeu com sucesso")
                        return True
                    else:
                        print(f"❌ Script do GA retornou erro: {ga_response.status_code}")
                        return False
                except:
                    print("❌ Erro ao carregar script do GA")
                    return False
            else:
                print("❌ Script do GA não encontrado")
                return False
        else:
            print("❌ ID não encontrado no código")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao testar: {e}")
        return False

def verificar_propriedade_ga():
    """Verifica propriedades do Google Analytics"""
    print("=" * 60)
    print("🔍 VERIFICAÇÃO DE PROPRIEDADES GOOGLE ANALYTICS")
    print("=" * 60)
    print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Site: {SITE_URL}")
    
    resultados = []
    
    for ga_id in GA_IDS_TESTE:
        if ga_id != "G-XXXXXXXXXX" and ga_id != "UA-XXXXXXXXX-1":
            resultado = testar_id_ga(ga_id)
            resultados.append((ga_id, resultado))
    
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES")
    print("=" * 60)
    
    for ga_id, resultado in resultados:
        status = "✅ FUNCIONANDO" if resultado else "❌ PROBLEMA"
        print(f"{ga_id}: {status}")
    
    print("\n" + "=" * 60)
    print("💡 COMO VERIFICAR SE A PROPRIEDADE EXISTE:")
    print("=" * 60)
    print("1. Acesse: https://analytics.google.com")
    print("2. Faça login com sua conta Google")
    print("3. Procure por 'Sintonize' na lista de propriedades")
    print("4. Verifique se o ID começa com 'G-'")
    print("5. Clique na propriedade e vá em 'Relatórios' → 'Tempo real'")
    
    print("\n" + "=" * 60)
    print("🆔 COMO CRIAR UMA NOVA PROPRIEDADE:")
    print("=" * 60)
    print("1. No Google Analytics, clique em 'Criar propriedade'")
    print("2. Nome: 'Sintonize'")
    print("3. Tipo: 'Web'")
    print("4. URL: 'http://127.0.0.1:8000'")
    print("5. Copie o novo ID (formato: G-XXXXXXXXXX)")
    print("6. Substitua no código do site")
    
    print("\n" + "=" * 60)
    print("🎯 CONTA DE DEMONSTRAÇÃO:")
    print("=" * 60)
    print("Se quiser testar rapidamente:")
    print("1. Acesse: https://analytics.google.com/analytics/web/demoAccount")
    print("2. Use: Google Merchandise Store")
    print("3. ID de exemplo: G-9304153A6T")
    print("4. Substitua temporariamente para testar")
    
    print("\n" + "=" * 60)
    print("🚀 PRÓXIMOS PASSOS:")
    print("=" * 60)
    if any(resultado for _, resultado in resultados):
        print("✅ Pelo menos um ID está funcionando!")
        print("✅ Verifique os dados no Google Analytics")
    else:
        print("❌ Nenhum ID está funcionando")
        print("💡 Crie uma nova propriedade ou use conta de demonstração")
    
    print("=" * 60)

if __name__ == "__main__":
    verificar_propriedade_ga() 