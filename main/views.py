# views.py
from django.shortcuts import render, redirect
from .forms import EscolhaForm, EscolhaForm2, EscolhaForm3, EscolhaForm4
from requests.exceptions import Timeout
import requests

def trilha_do_conhecimento(request):
    return render(request, 'trilha.html')


def index_view(request):
    return render(request, 'index.html')

def escolha1_view(request):
    if request.method == 'POST':
        form = EscolhaForm(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta1': form.cleaned_data['pergunta1'],
                'pergunta2': form.cleaned_data['pergunta2'],
                'pergunta3': form.cleaned_data['pergunta3'],
                'pergunta4': form.cleaned_data['pergunta4'],
                'pergunta5': form.cleaned_data['pergunta5'],
            }
            request.session['escolhas1'] = escolhas
            return redirect('escolha2')
    else:
        form = EscolhaForm()
    return render(request, 'escolha1.html', {'form': form})

def escolha2_view(request):
    if request.method == 'POST':
        form = EscolhaForm2(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta6': form.cleaned_data['pergunta6'],
                'pergunta7': form.cleaned_data['pergunta7'],
                'pergunta8': form.cleaned_data['pergunta8'],
                'pergunta9': form.cleaned_data['pergunta9'],
                'pergunta10': form.cleaned_data['pergunta10'],
            }
            request.session['escolhas2'] = escolhas
            return redirect('escolha3')
    else:
        form = EscolhaForm2()
    return render(request, 'escolha2.html', {'form': form})

def escolha3_view(request):
    if request.method == 'POST':
        form = EscolhaForm3(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta11': form.cleaned_data['pergunta11'],
                'pergunta12': form.cleaned_data['pergunta12'],
                'pergunta13': form.cleaned_data['pergunta13'],
                'pergunta14': form.cleaned_data['pergunta14'],
                'pergunta15': form.cleaned_data['pergunta15'],
            }
            request.session['escolhas3'] = escolhas
            return redirect('escolha4')
    else:
        form = EscolhaForm3()
    return render(request, 'escolha3.html', {'form': form})

def escolha4_view(request):
    if request.method == 'POST':
        form = EscolhaForm4(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta16': form.cleaned_data['pergunta16'],
                'pergunta17': form.cleaned_data['pergunta17'],
                'pergunta18': form.cleaned_data['pergunta18'],
                'pergunta19': form.cleaned_data['pergunta19'],
                'pergunta20': form.cleaned_data['pergunta20'],
            }
            request.session['escolhas4'] = escolhas
            return redirect('resultado')
    else:
        form = EscolhaForm4()
    return render(request, 'escolha4.html', {'form': form})


def resultado_view(request):
    escolhas = {
        'escolhas1': request.session.get('escolhas1', {}),
        'escolhas2': request.session.get('escolhas2', {}),
        'escolhas3': request.session.get('escolhas3', {}),
        'escolhas4': request.session.get('escolhas4', {}),
        
    }

    # Contar quantas vezes cada alternativa foi escolhida
    contagem = {
        'opcao1': 0,
        'opcao2': 0,
        'opcao3': 0,
        'opcao4': 0,
        'opcao5': 0,
    }
    
    for escolhas_form in escolhas.values():
        for escolha in escolhas_form.values():
            if escolha in contagem:
                contagem[escolha] += 1

    # Calcular os valores ponderados
    opcao1_count = contagem['opcao1']
    opcao2_count = contagem['opcao2'] * 2
    opcao3_count = contagem['opcao3'] * 3
    opcao4_count = contagem['opcao4'] * 4
    opcao5_count = contagem['opcao5'] * 5
    total = opcao1_count + opcao2_count + opcao3_count + opcao4_count + opcao5_count

    frase = ""

    if total < 21:
        frase = "Nenhum indício aparente de Síndrome de Burnout."
    elif 21 <= total <= 40:
        frase = "Possibilidade de desenvolver recomendações de prevenção da Síndrome de Burnout. Procure trabalhar as recomendações para prevenir o aumento do risco."
    elif 41 <= total <= 60:
        frase = "Fase inicial do Burnout. Procure ajuda profissional para debelar os sintomas e garantir, assim, a qualidade no desempenho profissional e sua qualidade de vida."
    elif 61 <= total <= 80:
        frase = "A Síndrome está instalada. Procure ajuda profissional para trabalhar com foco nos sintomas e na melhoria da qualidade dos resultados obtidos."
    elif 81 <= total <= 100:
        frase = "Você pode estar em uma fase considerável do Burnout, mas esse é um ponto em que é reversível e que sua confiança e nível de produtividade podem ser recuperados. Procure tratamento quanto antes."
    else:
        frase = "Algo deu errado"
    return render(request, 'resultado.html', {
        'contagem': contagem,
        'total': total,
        'frase': frase,
    })

def home_view(request):
    try:
        # O timeout está configurado para 1 segundo
        response = requests.get("http://equilibra-production.up.railway.app", timeout=0.1)
        # Apenas tenta acessar o JSON se a requisição for bem-sucedida
        frase_efeito = response.json().get("frase", "Frase padrão caso falhe a API.")
    except Timeout:
        # Caso a API demore mais de 3 segundos, usamos a frase padrão
        frase_efeito = "Frase padrão caso a API tenha demorado mais de 1 segundos."
    except requests.RequestException as e:
        # Para outros erros de requisição, use a frase padrão
        frase_efeito = "Frase padrão caso a API falhe."

    context = {
        'frase_efeito': frase_efeito,
        'logo_url': 'caminho/para/sua/logo.png', 
    }
    return render(request, 'home.html', context)

def sondagem(request):
    # Sua lógica para a view aqui
    return render(request, 'sondagem.html') 

def politicas_privacidade(request):
    return render(request, 'politicas_privacidade.html') 