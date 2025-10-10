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
from .analytics_client import get_analytics_client, get_report, get_active_users, get_event_count, format_report_data, get_form_abandonment_data, PROPERTY_ID
from google.analytics.data_v1beta.types import Dimension, Metric



def index (request):
    return render (request, 'index.html')

def politicas_privacidade (request):
    return render(request, 'politicas_privacidade.html')

def sondagem(request):
    if request.method == 'POST':
        form = BurnoutSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            score = survey.total_score()
            return redirect('resultado', score=score)
    else:
        form = BurnoutSurveyForm()

    return render(request, 'sondagem.html', {'form': form})

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
        "none": "Ótimo trabalho em cuidar de si! Que tal explorar nossa <a href='/trilha/'>trilha de conhecimento sobre burnout</a>? Ou manter seu bem-estar com uma <a href='/respiracao_guiada/'>sessão de respiração guiada</a> ou um <a href='/pomodoro/'>Pomodoro</a> para manter o foco sem esgotar sua energia?",
        "cuidado": "Pequenos cuidados fazem toda a diferença. Você pode aprender mais na nossa <a href='/trilha/'>trilha de conhecimento</a> ou fazer uma <a href='/respiracao_guiada/'>pausa consciente com a respiração guiada</a>. Nosso <a href='/pomodoro/'>Pomodoro online</a> pode ajudar a evitar sobrecarga.",
        "alerta": "Agora é um ótimo momento para agir! Conheça técnicas eficazes na <a href='/trilha/'>trilha de conhecimento</a>, experimente um <a href='/pomodoro/'>Pomodoro estruturado</a> ou pratique nossa <a href='/respiracao_guiada/'>respiração guiada para relaxar</a>.",
        "atencao": "Sabemos que esse momento pode ser difícil. Recomendamos consultar um profissional e, aqui no site, você pode encontrar apoio com a <a href='/trilha/'>trilha de conhecimento</a>, <a href='/respiracao_guiada/'>exercícios de respiração</a> e um <a href='/pomodoro/'>Pomodoro adaptado para você</a>.",
        "critico": "É fundamental procurar ajuda médica agora. Enquanto isso, você pode acessar nossa <a href='/trilha/'>trilha de conhecimento</a> e, se sentir confortável, usar a <a href='/respiracao_guiada/'>respiração guiada</a> como primeiro passo de autocuidado.",
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
    try:
        client = get_analytics_client()
        
        # Obter estatísticas para os cartões
        today = datetime.now().strftime('%Y-%m-%d')
        start_of_week = (datetime.now() - timedelta(days=datetime.now().weekday())).strftime('%Y-%m-%d')
        start_of_month = datetime.now().replace(day=1).strftime('%Y-%m-%d')

        visitors_today_response = get_report(client, PROPERTY_ID, today, today, [], [Metric(name='totalUsers')])
        visitors_week_response = get_report(client, PROPERTY_ID, start_of_week, today, [], [Metric(name='totalUsers')])
        visitors_month_response = get_report(client, PROPERTY_ID, start_of_month, today, [], [Metric(name='totalUsers')])
        
        stats = {
            'total_visitors_today': int(visitors_today_response.rows[0].metric_values[0].value) if visitors_today_response.rows else 0,
            'total_visitors_week': int(visitors_week_response.rows[0].metric_values[0].value) if visitors_week_response.rows else 0,
            'total_visitors_month': int(visitors_month_response.rows[0].metric_values[0].value) if visitors_month_response.rows else 0,
            'last_updated': timezone.now()
        }
        
        return render(request, 'analytics/dashboard.html', {'stats': stats})

    except Exception as e:
        # Em caso de erro (ex: credenciais inválidas), exibe uma mensagem amigável
        # e renderiza o painel com dados zerados para não quebrar a página.
        messages.error(request, f"Erro ao conectar com o Google Analytics: {e}. Verifique a configuração.")
        stats = {
            'total_visitors_today': 0,
            'total_visitors_week': 0,
            'total_visitors_month': 0,
            'last_updated': timezone.now()
        }
        return render(request, 'analytics/dashboard.html', {'stats': stats})

@login_required
def analytics_export(request):
    """Exporta dados do Google Analytics para CSV ou JSON."""
    formato = request.GET.get('formato', 'csv')
    periodo = request.GET.get('periodo', 'week')

    end_date = datetime.now().strftime('%Y-%m-%d')
    if periodo == 'day':
        start_date = end_date
    elif periodo == 'month':
        start_date = (datetime.now().replace(day=1)).strftime('%Y-%m-%d')
    else: # week
        start_date = (datetime.now() - timedelta(days=datetime.now().weekday())).strftime('%Y-%m-%d')

    try:
        client = get_analytics_client()
        
        # Obter dados de páginas populares para o período selecionado
        pages_response = get_report(
            client,
            PROPERTY_ID,
            start_date,
            end_date,
            [Dimension(name='pageTitle')],
            [Metric(name='screenPageViews')]
        )
        paginas_populares = format_report_data(pages_response, 'titulo', 'visualizacoes')
        
        if formato == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="analytics_export_{periodo}.csv"'
            
            writer = csv.writer(response)
            writer.writerow(['Página', 'Visualizações'])
            for pagina in paginas_populares:
                writer.writerow([pagina['titulo'], pagina['visualizacoes']])
            
            return response

        elif formato == 'json':
            return JsonResponse({
                'periodo': periodo,
                'paginas_populares': paginas_populares
            }, json_dumps_params={'indent': 2})

    except Exception as e:
        return HttpResponse(f"Erro ao exportar dados: {e}", status=500)


@login_required
def analytics_api(request):
    """API para fornecer dados do Google Analytics ao frontend."""
    try:
        client = get_analytics_client()
        periodo = request.GET.get('periodo', 'week')

        # Define as datas com base no período
        end_date = datetime.now().strftime('%Y-%m-%d')
        if periodo == 'day':
            start_date = end_date
        elif periodo == 'week':
            start_date = (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d')
        elif periodo == 'month':
            start_date = (datetime.now() - timedelta(days=29)).strftime('%Y-%m-%d')
        else:
            start_date = (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d')

        # 1. Visitantes por dia (para o gráfico)
        visitors_per_day_response = get_report(
            client, PROPERTY_ID, start_date, end_date,
            [Dimension(name='date')],
            [Metric(name='totalUsers')]
        )
        visitors_per_day = [
            {'data': datetime.strptime(row.dimension_values[0].value, '%Y%m%d').strftime('%d/%m'), 'visitantes': int(row.metric_values[0].value)}
            for row in visitors_per_day_response.rows
        ]

        # 2. Dispositivos
        devices_response = get_report(
            client, PROPERTY_ID, start_date, end_date,
            [Dimension(name='deviceCategory')],
            [Metric(name='totalUsers')]
        )
        devices_data = {row.dimension_values[0].value.lower(): int(row.metric_values[0].value) for row in devices_response.rows}
        
        # 3. Páginas mais populares
        pages_response = get_report(
            client, PROPERTY_ID, start_date, end_date,
            [Dimension(name='pageTitle')],
            [Metric(name='screenPageViews')],
            # Adicionar ordenação aqui se a API suportar
        )
        popular_pages = format_report_data(pages_response, 'titulo', 'visualizacoes')

        # 4. Fontes de tráfego
        traffic_response = get_report(
            client, PROPERTY_ID, start_date, end_date,
            [Dimension(name='sessionSource')],
            [Metric(name='totalUsers')]
        )
        traffic_sources_raw = format_report_data(traffic_response, 'fonte', 'visitantes')
        total_visitors_period = sum(item['visitantes'] for item in traffic_sources_raw)
        traffic_sources = [
            {**item, 'percentual': round((item['visitantes'] / total_visitors_period) * 100, 1) if total_visitors_period > 0 else 0}
            for item in traffic_sources_raw
        ]
        
        # 5. Dados em tempo real
        active_users = get_active_users(client, PROPERTY_ID)

        # 6. Contagem de eventos específicos
        sondagem_starts = get_event_count(client, PROPERTY_ID, start_date, end_date, 'inicio_teste_burnout')
        sondagem_completes = get_event_count(client, PROPERTY_ID, start_date, end_date, 'conclusao_formulario')

        # 7. Dados de abandono do formulário
        abandono_formulario = get_form_abandonment_data(client, PROPERTY_ID, start_date, end_date)

        # Monta a resposta final
        data = {
            'visitantes_por_dia': sorted(visitors_per_day, key=lambda x: datetime.strptime(x['data'], '%d/%m')),
            'dispositivos': {
                'desktop': devices_data.get('desktop', 0),
                'mobile': devices_data.get('mobile', 0),
                'tablet': devices_data.get('tablet', 0),
            },
            'paginas_populares': popular_pages[:10], # Limita a 10
            'fontes_trafego': traffic_sources[:10], # Limita a 10
            'dados_tempo_real': {
                'usuarios_ativos': active_users,
            },
            'eventos': {
                'sondagem_inicios': sondagem_starts,
                'sondagem_conclusoes': sondagem_completes,
            },
            'abandono_formulario': abandono_formulario,
             # Incluir totais para os cartões principais, se necessário (exemplo)
            'visitantes_hoje': get_report(client, PROPERTY_ID, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows[0].metric_values[0].value if get_report(client, PROPERTY_ID, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows else 0,
            'visitantes_semana': get_report(client, PROPERTY_ID, (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows[0].metric_values[0].value if get_report(client, PROPERTY_ID, (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows else 0,
            'visitantes_mes': get_report(client, PROPERTY_ID, (datetime.now() - timedelta(days=29)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows[0].metric_values[0].value if get_report(client, PROPERTY_ID, (datetime.now() - timedelta(days=29)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), [], [Metric(name='totalUsers')]).rows else 0,
        }
        
        return JsonResponse(data)

    except Exception as e:
        # Log do erro para depuração
        print(f"Erro na API de Analytics: {e}")
        # Retorna uma resposta de erro clara para o frontend
        return JsonResponse({'error': 'Não foi possível obter os dados do Google Analytics. Verifique a configuração e as permissões da API.'}, status=500)
