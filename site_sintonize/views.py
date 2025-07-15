from django.shortcuts import render, redirect
from requests.exceptions import Timeout
from .forms import BurnoutSurveyForm
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
import json
import csv



def index (request):
    return render (request, 'index.html')

def politicas_privacidade (request):
    return render(request, 'politicas_privacidade.html')

def sondagem (requests):
    return render (requests, 'sondagem.html')

def sobre_nos (request):
    return render(request, 'sobre_nos.html') 

def equipe (request):
    return render(request, 'equipe.html') 

def trilha (request):
    return render(request, 'trilha.html') 

def diagnostico (request):
    return render(request, 'diagnostico.html') 

def tratamento (request):
    return render(request, 'tratamento.html') 

def pomodoro (request):
    return render(request, 'pomodoro.html')

def respiracao_guiada (request):
    return render(request, 'respiracao_guiada.html')



def search_options(request):
    query = request.GET.get('query', '')
    # Aqui você deve substituir isso pelos seus dados reais
    options = ["Burnout", " Teste", " ", " ", ""]
    filtered_options = [option for option in options if query.lower() in option.lower()]
    
    return JsonResponse(filtered_options, safe=False)


def equipe(request):
    membros = [
        {
            'nome': 'Alex Calado',
            'cargo': 'Product Owner',
            'descricao': '“Sou um entusiasta da experiência do usuário e acredito que um produto de sucesso é aquele que coloca as necessidades do usuário em primeiro lugar! Minha missão é transformar ideias em produtos digitais que gerem valor real para os nossos usuários”',
            'linkedin': 'https://www.linkedin.com/in/alexcalado/',
            'imagem': 'images/alex.png',  # URL da imagem do membro
        },
     
        {
            'nome': 'Paulo Roberto',
            'cargo': 'Quality Assurance',
            'descricao': '"Sou formado em Análise e Desenvolvimento de Sistemas e atualmente estou cursando uma pós-graduação em Teste de Software pela Universidade Cruzeiro do Sul. Também estou participando do curso CTG 2.0 (Comunidade de Testers Global), ministrado por Vinícius Pessoni. Estou sempre em busca de novos conhecimentos para impulsionar meu crescimento como QA."',
            'linkedin': 'https://www.linkedin.com/in/paulinnrs/',
            'imagem': 'images/paulo.png',  # URL da imagem do membro
        },

          {
            'nome': 'Jéssica Carvalho',
            'cargo': 'Front End Developer',
            'descricao': '"Estou me formando em Desenvolvimento Full Stack. Atuo como desenvolvedora Front-End no Projeto Sintonize e sou apaixonada por tecnologia. Atualmente em transição de carreira e estou sempre buscando novas oportunidades para aprender, crescer profissionalmente e contribuir de forma significativa para minha equipe. Acredito que é possível criar experiências digitais incríveis quando unimos boas práticas e desenvolvimento!"',
            'linkedin': 'https://www.linkedin.com/in/jessica-carvalho30',
            'imagem': 'images/jess.png',  # URL da imagem do membro
        },
       
          {
            'nome': 'Fernando Galvão',
            'cargo': 'Scrum Master',
            'descricao': '"Ser um agente de transformação digital é o que me move para alcançar horizontes desconhecidos.” Em 2019, iniciei um processo de transição de carreira para a área de dados, criando dashboards interativos e relatórios personalizados para monitoramento contínuo de KPIs e métricas de negócios através das ferramentas Power BI e Qlik Sense. Desde 2022 comecei a embarcar em um novo horizonte, o universo ágil. Diante disso, desenvolver habilidades de um agilista tornou-se um caminho sem volta, pois, não só passei a adquirir conhecimentos bem como replicá-los para outros profissionais que são entusiastas ou que estejam iniciando a carreira na área. Possuo as seguintes certificações: Professional Scrum Master 1 (PSM 1), Accredited Scrum Fundamentals Certification, Lean Agile Coach Professional e Management 3.0 Foundation Workshop."',
            'linkedin': 'https://linkedin.com/in/fernandomgalvao/',
            'imagem': 'images/galvao.png',  #
        },
        
          {
            'nome': 'Bruna Lacerda',
            'cargo': 'Quality Assurance',
            'descricao': '"Sou uma profissional de QA com 3 anos de experiência em uma empresa de tecnologia, responsável por garantir a qualidade de produtos e serviços. Com atuação anterior em web design e atendimento ao cliente, tenho uma visão orientada à experiência do usuário. Sou curiosa e gosto de explorar e conhecer novas áreas e pessoas!."',
            'linkedin': 'https://www.linkedin.com/in/brunajlacerda',
            'imagem': 'images/bru.png', 
        },
          {
            'nome': 'Eduardo Gonçalves Moraes',
            'cargo': 'Back End Developer',
            'descricao': '"Trabalho com desenvolvimento de sites e aplicativos web, gerencio e atualizo sites corporativos. Me especializando em Python na área de ciência de dados e aplicativos web, com ferramentas como pandas e django. Em busca de oportunidade para voltar ao mercado de trabalho, atualmente trabalho como freelancer."',
            'linkedin': 'https://www.linkedin.com/in/eduardo-moraes-285b9315a',
            'imagem': 'images/edu.png',  
        },
          {
            'nome': 'Monique da Hora',
            'cargo': 'Product Owner',
            'descricao': '"Iniciei minha carreira na área de tecnologia com montagem e manutenção de computadores, e posteriormente prestei serviços de suporte de TI para outras empresas. Sempre fui apaixonada por resolver problemas e, ao longo da minha trajetória, tive a oportunidade de criar produtos que geraram valor para as empresas. Sou curiosa e inovadora, e estou constantemente refletindo sobre como a tecnologia vai evoluir, impactar a sociedade e transformar os negócios no futuro."',
            'linkedin': 'https://www.linkedin.com/in/moniquedahora/',
            'imagem': 'images/monique.png',  
        },
        {
          'nome': 'Rhaíssa Alessi Manzini',
            'cargo': 'UX/UI Design',
            'descricao': '"Profissional com 10 anos de experiência na área Jurídica e Compliance em transição de carreira para UX/UI Design. Apaixonada por Design desde criança, hoje aplico minha paixão e expertise para criar soluções estratégicas alinhadas aos valores da companhia e objetivos do negócio."',
            'linkedin': 'https://www.linkedin.com/in/rha%C3%ADssa-manzini/',
            'imagem': 'images/rhaissa.png',  
        },
        {
            'nome': 'Myrella da Silva Pinto',
            'cargo': 'Scrum Master',
            'descricao': '"Atualmente estou em transição de carreira para a agilidade e, ajudar equipes a alcançar seu máximo potencial por meio da adoção das práticas ágeis se tornou uma paixão. Meu propósito é o de ser uma agente de transformação, criando soluções, gerando valor e, promovendo uma cultura de melhoria contínua dentro das equipes."',
            'linkedin': 'https://www.linkedin.com/in/mysilva/',
            'imagem': 'images/myrella.png',  
        },
          {
            'nome': 'Graziella Rodrigues',
            'cargo': 'Front End Developer',
            'descricao': '"Atualmente, estou me formando em Análise e Desenvolvimento de Sistemas. Sou apaixonada por tecnologia, estou constantemente em busca de oportunidades para aprender e crescer, tanto profissionalmente quanto pessoalmente. Acredito que, ao unir boas práticas de desenvolvimento com um olhar atento à experiência do usuário, é possível criar soluções digitais que impactem positivamente a vida das pessoas."',
            'linkedin': 'https://www.linkedin.com/in/agraziella',
            'imagem': 'images/grazi.png',  
        },
    ]
    return render(request, 'equipe.html', {'membros': membros})


def burnout_survey_view(request):
    if request.method == 'POST':
        form = BurnoutSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            score = survey.total_score()
            return redirect('resultado', score=score)
    else:
        form = BurnoutSurveyForm()

    return render(request, 'burnout_survey.html', {'form': form})

def resultado_view(request, score):

    icons = {
        "none": static("images/modal/icon1.png"),
        "cuidado": static("images/modal/icon2.png"),
        "alerta": static("images/modal/icon3.png"),
        "atencao": static("images/modal/icon4.png"),
        "critico": static("images/modal/icon5.png"),
    }
    
    # Dicionário de imagens de resultados
    imagens = {
        "none": static("images/modal/meditacao.png"),        
        "cuidado": static("images/modal/trabalho.png"),
        "alerta": static("images/modal/lupa1.png"),
        "atencao": static("images/modal/atencao.png"),
        "critico": static("images/modal/critico.png"),
    }
    
    # Defina as mensagens para cada pontuação
    mensagens = {
        "none": "Ótimo trabalho em cuidar de si! Que tal explorar nossa <a href='/trilha/' target='_blank'>trilha de conhecimento sobre burnout</a>? Ou manter seu bem-estar com uma <a href='/respiracao_guiada/' target='_blank'> sessão de respiração guiada </a> ou um <a href='/pomodoro.html' target='_blank'> Pomodoro </a> para manter o foco sem esgotar sua energia?",
        "cuidado": "Pequenos cuidados fazem toda a diferença. Você pode aprender mais na nossa  <a href='/trilha/' target='_blank'>trilha de conhecimento</a> ou fazer uma<a href='/respiracao_guiada/' target='_blank'> pausa consciente com a  respiração guiada </a>. Nosso<a href='/pomodoro.html' target='_blank'> Pomodoro online</a> pode ajudar a evitar sobrecarga.",
        "alerta": "Agora é um ótimo momento para agir! Conheça técnicas eficazes na <a href='/trilha/' target='_blank'>trilha de conhecimento</a>, experimente um<a href='/pomodoro.html' target='_blank'> Pomodoro estruturado</a> ou pratique nossa<a href='/respiracao_guiada' target='_blank'> respiração guiada para relaxar. </a>",
        "atencao": "Sabemos que esse momento pode ser difícil. Recomendamos consultar um profissional e, aqui no site, você pode encontrar apoio com a <a href='/trilha/' target='_blank'>trilha de conhecimento</a>,<a href='/respiracao_guiada/' target='_blank'> exercícios de respiração </a> e um <a href='/pomodoro.html' target='_blank'>  Pomodoro adaptado para você </a>.",
        "critico": "É fundamental procurar ajuda médica agora. Enquanto isso, você pode acessar nossa  <a href='/trilha/' target='_blank'>trilha de conhecimento</a> e, se sentir confortável, usar a <a href='/respiracao_guiada/' target='_blank'> respiração guiada </a> como primeiro passo de autocuidado.",
    }


    # Determine o texto do resultado, a imagem e a mensagem com base na pontuação
    if score > 60:
        return JsonResponse({
            'error': True,
            'message': 'Pontuação inválida. O score máximo permitido é 60.'
        }, status=400)

    
    if score <= 20:
        icon = icons["none"]
        result_text = mensagens["none"]
        title = "Tudo sob controle! Continue assim"
        image = imagens["none"]
        user_message = mensagens["none"]
    
    elif 21 <= score <= 30:
        result_text = mensagens["cuidado"]
        icon = icons["cuidado"]
        title = "Fique de olho! Pequenos sinais de estresse"
        image = imagens["cuidado"]
        user_message = mensagens["cuidado"]

    elif 31 <= score <= 40:
        icon = icons["alerta"]
        result_text = mensagens["alerta"]
        title = "Possível Risco de Burnout! Hora de Prevenir"
        image = imagens["alerta"]
        user_message = mensagens["alerta"]

    elif 41 <= score <= 50:
        icon = icons["atencao"]
        result_text = mensagens["atencao"]
        title = "Risco Alto de Burnout! Procure Ajuda "
        image = imagens["atencao"]
        user_message = mensagens["atencao"]

    elif 51 <= score <= 60:
        icon = icons["critico"]
        result_text = mensagens["critico"]
        title = "Nível Crítico de Burnout! Procure Ajuda "
        image = imagens["critico"]
        user_message = mensagens["critico"]

    # Retorne um JsonResponse com os dados necessários para o modal
    return JsonResponse({'title': title, 'body': result_text, 'image': image, 'userMessage': user_message, 'icon': icon})


@login_required
def analytics_dashboard(request):
    """Painel de monitoramento com Google Analytics"""
    
    # Dados simulados para demonstração (você pode remover após configurar o GA)
    hoje = timezone.now().date()
    
    # Estatísticas básicas simuladas - substituir por dados reais do GA4
    stats = {
        'total_visitors_today': 91,
        'total_visitors_week': 847,
        'total_visitors_month': 2456,
        'top_pages': [
            {'page': '/', 'title': 'Página Inicial', 'views': 456},
            {'page': '/sondagem.html', 'title': 'Sondagem de Burnout', 'views': 234},
            {'page': '/trilha/', 'title': 'Sobre o Burnout', 'views': 178},
            {'page': '/pomodoro/', 'title': 'Pomodoro', 'views': 134},
            {'page': '/respiracao_guiada/', 'title': 'Respiração Guiada', 'views': 89},
        ],
        'top_referrers': [
            {'source': 'Direto', 'visitors': 345, 'percentage': 40.7},
            {'source': 'Google', 'visitors': 234, 'percentage': 27.6},
            {'source': 'Redes Sociais', 'visitors': 156, 'percentage': 18.4},
            {'source': 'Referências', 'visitors': 78, 'percentage': 9.2},
        ],
        'device_breakdown': {
            'desktop': 456,
            'mobile': 312,
            'tablet': 79
        },
        'browser_breakdown': {
            'Chrome': 567,
            'Firefox': 123,
            'Safari': 89,
            'Edge': 45,
            'Outros': 23
        },
        'last_updated': timezone.now()
    }
    
    return render(request, 'analytics/dashboard.html', {
        'stats': stats,
        'today': hoje
    })


@login_required
def analytics_export(request):
    """Exportar dados do Google Analytics"""
    
    periodo = request.GET.get('periodo', 'week')  # day, week, month
    formato = request.GET.get('formato', 'csv')   # csv, json
    
    # Configurar datas baseado no período
    hoje = timezone.now().date()
    if periodo == 'day':
        data_inicio = hoje
        data_fim = hoje
    elif periodo == 'week':
        data_inicio = hoje - timedelta(days=7)
        data_fim = hoje
    elif periodo == 'month':
        data_inicio = hoje - timedelta(days=30)
        data_fim = hoje
    else:
        data_inicio = hoje - timedelta(days=7)
        data_fim = hoje
    
    # Dados simulados para exportação - substituir por dados reais do GA4
    dados = {
        'periodo': {
            'inicio': data_inicio.strftime('%Y-%m-%d'),
            'fim': data_fim.strftime('%Y-%m-%d')
        },
        'resumo': {
            'total_visitantes': 847,
            'total_visualizacoes': 1234,
            'taxa_rejeicao': 32.5,
            'tempo_medio_sessao': 145
        },
        'dados_diarios': [
            {'data': (hoje - timedelta(days=6)).strftime('%Y-%m-%d'), 'visitantes': 98, 'visualizacoes': 142},
            {'data': (hoje - timedelta(days=5)).strftime('%Y-%m-%d'), 'visitantes': 112, 'visualizacoes': 167},
            {'data': (hoje - timedelta(days=4)).strftime('%Y-%m-%d'), 'visitantes': 89, 'visualizacoes': 134},
            {'data': (hoje - timedelta(days=3)).strftime('%Y-%m-%d'), 'visitantes': 156, 'visualizacoes': 203},
            {'data': (hoje - timedelta(days=2)).strftime('%Y-%m-%d'), 'visitantes': 134, 'visualizacoes': 189},
            {'data': (hoje - timedelta(days=1)).strftime('%Y-%m-%d'), 'visitantes': 167, 'visualizacoes': 234},
            {'data': hoje.strftime('%Y-%m-%d'), 'visitantes': 91, 'visualizacoes': 165},
        ],
        'paginas_populares': [
            {'pagina': '/', 'titulo': 'Página Inicial', 'visualizacoes': 456},
            {'pagina': '/sondagem.html', 'titulo': 'Sondagem de Burnout', 'visualizacoes': 234},
            {'pagina': '/trilha/', 'titulo': 'Sobre o Burnout', 'visualizacoes': 178},
            {'pagina': '/pomodoro/', 'titulo': 'Pomodoro', 'visualizacoes': 134},
            {'pagina': '/respiracao_guiada/', 'titulo': 'Respiração Guiada', 'visualizacoes': 89},
        ],
        'fontes_trafego': [
            {'fonte': 'Direto', 'visitantes': 345, 'percentual': 40.7},
            {'fonte': 'Google', 'visitantes': 234, 'percentual': 27.6},
            {'fonte': 'Redes Sociais', 'visitantes': 156, 'percentual': 18.4},
            {'fonte': 'Referências', 'visitantes': 78, 'percentual': 9.2},
            {'fonte': 'Outros', 'visitantes': 34, 'percentual': 4.1},
        ],
        'dispositivos': {
            'desktop': 456,
            'mobile': 312,
            'tablet': 79
        },
        'navegadores': {
            'chrome': 567,
            'firefox': 123,
            'safari': 89,
            'edge': 45,
            'outros': 23
        },
        'gerado_em': timezone.now().isoformat()
    }
    
    if formato == 'json':
        response = HttpResponse(
            json.dumps(dados, indent=2, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
        response['Content-Disposition'] = f'attachment; filename="analytics_sintonize_{periodo}_{hoje}.json"'
        
        # Rastrear download
        return response
    
    elif formato == 'csv':
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename="analytics_sintonize_{periodo}_{hoje}.csv"'
        
        writer = csv.writer(response)
        
        # Cabeçalho do CSV
        writer.writerow(['Relatório de Analytics - Sintonize'])
        writer.writerow(['Período:', f"{data_inicio} até {data_fim}"])
        writer.writerow(['Gerado em:', timezone.now().strftime('%Y-%m-%d %H:%M:%S')])
        writer.writerow([])
        
        # Resumo
        writer.writerow(['RESUMO'])
        writer.writerow(['Total de Visitantes:', dados['resumo']['total_visitantes']])
        writer.writerow(['Total de Visualizações:', dados['resumo']['total_visualizacoes']])
        writer.writerow(['Taxa de Rejeição:', f"{dados['resumo']['taxa_rejeicao']}%"])
        writer.writerow(['Tempo Médio de Sessão:', f"{dados['resumo']['tempo_medio_sessao']} segundos"])
        writer.writerow([])
        
        # Dados diários
        writer.writerow(['DADOS DIÁRIOS'])
        writer.writerow(['Data', 'Visitantes', 'Visualizações'])
        for dia in dados['dados_diarios']:
            writer.writerow([dia['data'], dia['visitantes'], dia['visualizacoes']])
        writer.writerow([])
        
        # Páginas populares
        writer.writerow(['PÁGINAS MAIS VISITADAS'])
        writer.writerow(['Página', 'Título', 'Visualizações'])
        for pagina in dados['paginas_populares']:
            writer.writerow([pagina['pagina'], pagina['titulo'], pagina['visualizacoes']])
        writer.writerow([])
        
        # Fontes de tráfego
        writer.writerow(['FONTES DE TRÁFEGO'])
        writer.writerow(['Fonte', 'Visitantes', 'Percentual'])
        for fonte in dados['fontes_trafego']:
            writer.writerow([fonte['fonte'], fonte['visitantes'], f"{fonte['percentual']}%"])
        writer.writerow([])
        
        # Dispositivos
        writer.writerow(['DISPOSITIVOS'])
        writer.writerow(['Tipo', 'Quantidade'])
        for dispositivo, quantidade in dados['dispositivos'].items():
            writer.writerow([dispositivo.title(), quantidade])
        writer.writerow([])
        
        # Navegadores
        writer.writerow(['NAVEGADORES'])
        writer.writerow(['Navegador', 'Quantidade'])
        for navegador, quantidade in dados['navegadores'].items():
            writer.writerow([navegador.title(), quantidade])
        
        return response
    
    else:
        return JsonResponse({'error': 'Formato não suportado'}, status=400)


def analytics_api(request):
    """API para fornecer dados do Google Analytics via AJAX"""
    
    periodo = request.GET.get('periodo', 'week')
    
    # Aqui você integraria com a API do Google Analytics
    # Por enquanto, retornamos dados simulados
    
    # Dados de demonstração (será substituído por dados reais em 24-48h)
    dados = {
        'visitantes_hoje': 12,
        'visitantes_semana': 89,
        'visitantes_mes': 324,
        'paginas_populares': [
            {'pagina': '/', 'titulo': 'Página Inicial', 'visualizacoes': 145},
            {'pagina': '/sondagem.html', 'titulo': 'Sondagem de Burnout', 'visualizacoes': 89},
            {'pagina': '/trilha/', 'titulo': 'Trilha de Conhecimento', 'visualizacoes': 67},
            {'pagina': '/sobre_nos/', 'titulo': 'Sobre Nós', 'visualizacoes': 34},
            {'pagina': '/equipe/', 'titulo': 'Equipe', 'visualizacoes': 23},
        ],
        'fontes_trafego': [
            {'fonte': 'Direto', 'visitantes': 152, 'percentual': 47},
            {'fonte': 'Google', 'visitantes': 98, 'percentual': 30},
            {'fonte': 'Redes Sociais', 'visitantes': 45, 'percentual': 14},
            {'fonte': 'Outros', 'visitantes': 29, 'percentual': 9},
        ],
        'dispositivos': {
            'desktop': 178,
            'mobile': 125,
            'tablet': 21
        },
        'dados_tempo_real': {
            'usuarios_ativos': 3,
            'paginas_ativas': ['/', '/sondagem.html', '/trilha/']
        }
    }
    
    return JsonResponse(dados)
