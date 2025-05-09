from django.shortcuts import render, redirect
from requests.exceptions import Timeout
from .forms import BurnoutSurveyForm
from django.http import JsonResponse
from django.contrib import messages
from django.templatetags.static import static



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
        "cuidado": "Pequenos cuidados fazem toda a diferença. Você pode aprender mais na nossa  <a href='/trilha/' target='_blank'>trilha de conhecimento</a> ou fazer uma <a href='/respiracao_guiada/' target='_blank'> pausa consciente com a  respiração guiada </a>. Nosso<a href='/pomodoro.html' target='_blank'> Pomodoro online </a>pode ajudar a evitar sobrecarga.",
        "alerta": "Agora é um ótimo momento para agir! Conheça técnicas eficazes na <a href='/trilha/' target='_blank'>trilha de conhecimento</a>, experimente um  <a href='/pomodoro.html' target='_blank'> Pomodoro estruturado</a> ou pratique nossa<a href='/respiracao_guiada' target='_blank'> respiração guiada para relaxar. </a>",
        "atencao": "Sabemos que esse momento pode ser difícil. Recomendamos consultar um profissional e, aqui no site, você pode encontrar apoio com a <a href='/trilha/' target='_blank'>trilha de conhecimento</a>,<a href='/respiracao_guiada/' target='_blank'> exercícios de respiração </a> e um <a href='/pomodoro.html' target='_blank'>  Pomodoro adaptado para você </a>.",
        "critico": "É fundamental procurar ajuda médica agora. Enquanto isso, você pode acessar nossa  <a href='/trilha/' target='_blank'>trilha de conhecimento</a> e, se sentir confortável, usar a <a href='/respiracao_guiada/' target='_blank'> respiração guiada </a> como primeiro passo de autocuidado.",
    }

    # Determine o texto do resultado, a imagem e a mensagem com base na pontuação
    if score <= 20:
        icon = icons["none"]
        result_text = "Parabéns! Seu nível de estresse está bem equilibrado, sem sinais de Burnout."
        title = "Tudo sob controle! Continue assim"
        image = imagens["none"]
        user_message = mensagens["none"]
    
    elif 21 <= score <= 30:
        result_text = "Possibilidade de desenvolver recomendações de prevenção da Síndrome de Burnout."
        icon = icons["cuidado"]
        title = "Fique de olho! Pequenos sinais de estresse"
        image = imagens["cuidado"]
        user_message = mensagens["cuidado"]

    elif 31 <= score <= 40:
        icon = icons["alerta"]
        result_text = "Atenção! Alguns sintomas de Burnout podem começar a aparecer. "
        title = "Possível Risco de Burnout! Hora de Prevenir"
        image = imagens["alerta"]
        user_message = mensagens["alerta"]

    elif 41 <= score <= 50:
        icon = icons["atencao"]
        result_text = "Atenção! Alguns sintomas de Burnout podem começar a aparecer. "
        title = "Risco Alto de Burnout! Procure Ajuda "
        image = imagens["atencao"]
        user_message = mensagens["atencao"]

    elif 51 <= score <= 60:
        icon = icons["critico"]
        result_text = "Você pode estar em uma fase considerável do Burnout. Procure tratamento."
        title = "Nível Crítico de Burnout! Procure Ajuda "
        image = imagens["critico"]
        user_message = mensagens["critico"]

    # Retorne um JsonResponse com os dados necessários para o modal
    return JsonResponse({'title': title, 'body': result_text, 'image': image, 'userMessage': user_message, 'icon': icon})
