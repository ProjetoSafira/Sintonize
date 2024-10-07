from django.shortcuts import render, redirect
from requests.exceptions import Timeout
import requests

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
            'nome': 'Fernanda Giglio',
            'cargo': 'UX/UI Design',
            'descricao': '"Profissional com 10 anos de experiência em atendimento ao cliente e área comercial, formada em Publicidade e Propaganda. Estou em transição para o Design UX/UI, onde utilizo minhas habilidades de comunicação, empatia e resolução de problemas para melhorar a experiência dos usuários. Com passagens por startups de tecnologia, tenho uma visão estratégica voltada para resultados e estou sempre em busca de novas oportunidades para crescer. Além disso, tenho experiência em marketing, vendas e suporte a franqueados, sempre priorizando a satisfação do cliente',
            'linkedin': 'https://www.linkedin.com/in/fernandagiglio/',
            'imagem': 'images/fer.png',  # URL da imagem do membro
        },
          {
            'nome': 'Fernando Galvão',
            'cargo': 'Scrum Master',
            'descricao': '"Ser um agente de transformação digital é o que me move para alcançar horizontes desconhecidos.” Em 2019, iniciei um processo de transição de carreira para a área de dados, criando dashboards interativos e relatórios personalizados para monitoramento contínuo de KPIs e métricas de negócios através das ferramentas Power BI e Qlik Sense. Desde 2022 comecei a embarcar em um novo horizonte, o universo ágil. Diante disso, desenvolver habilidades de um agilista tornou-se um caminho sem volta, pois, não só passei a adquirir conhecimentos bem como replicá-los para outros profissionais que são entusiastas ou que estejam iniciando a carreira na área. Possuo as seguintes certificações: Professional Scrum Master 1 (PSM 1), Accredited Scrum Fundamentals Certification, Lean Agile Coach Professional e Management 3.0 Foundation Workshop."',
            'linkedin': 'https://linkedin.com/in/fernandomgalvao/',
            'imagem': 'images/fernando.png',  # URL da imagem do membro
        },
          {
            'nome': 'Jefferson Bernardes',
            'cargo': 'Scrum Master',
            'descricao': '"Gestão e gerenciamento de projetos, desenvolvimento e implantação de soluções de alto nível, atendendo aos diversos segmentos na indústria farmacêutica, contemplando diferentes regras de negócios no segmento de logística, projetos de grande complexidade com diversas áreas envolvidas, onde absorvi experiência na mitigação dos riscos e gestão de grandes resultados. Atuação no controle das atividades mapeadas e levantadas para desenvolvimento do projeto."',
            'linkedin': 'https://www.linkedin.com/in/jefferson-bernardes-109584a8',
            'imagem': 'images/jefferson.png',  # URL da imagem do membro
        },
          {
            'nome': 'Bruna Lacerda',
            'cargo': 'Quality Assurance',
            'descricao': '"Sou uma profissional de QA com 3 anos de experiência em uma empresa de tecnologia, responsável por garantir a qualidade de produtos e serviços. Com atuação anterior em web design e atendimento ao cliente, tenho uma visão orientada à experiência do usuário. Sou curiosa e gosto de explorar e conhecer novas áreas e pessoas!."',
            'linkedin': 'https://www.linkedin.com/in/brunajlacerda',
            'imagem': 'images/bru.png',  # URL da imagem do membro
        },
          {
            'nome': 'Eduardo Gonçalves Moraes',
            'cargo': 'Back End Developer',
            'descricao': '"Trabalho com desenvolvimento de sites e aplicativos web, gerencio e atualizo sites corporativos. Me especializando em Python na área de ciência de dados e aplicativos web, com ferramentas como pandas e django. Em busca de oportunidade para voltar ao mercado de trabalho, atualmente trabalho como freelancer."',
            'linkedin': 'https://www.linkedin.com/in/eduardo-moraes-285b9315a',
            'imagem': 'images/edu.png',  # URL da imagem do membro
        },
          {
            'nome': 'Monique da Hora',
            'cargo': 'Product Owner',
            'descricao': '"Iniciei minha carreira na área de tecnologia com montagem e manutenção de computadores, e posteriormente prestei serviços de suporte de TI para outras empresas. Sempre fui apaixonada por resolver problemas e, ao longo da minha trajetória, tive a oportunidade de criar produtos que geraram valor para as empresas. Sou curiosa e inovadora, e estou constantemente refletindo sobre como a tecnologia vai evoluir, impactar a sociedade e transformar os negócios no futuro."',
            'linkedin': 'https://www.linkedin.com/in/moniquedahora/',
            'imagem': 'images/monique.png',  # URL da imagem do membro
        },
        {
          'nome': 'Rhaíssa Alessi Manzini',
            'cargo': 'UX/UI Design',
            'descricao': '"Profissional com 10 anos de experiência na área Jurídica e Compliance em transição de carreira para UX/UI Design. Apaixonada por Design desde criança, hoje aplico minha paixão e expertise para criar soluções estratégicas alinhadas aos valores da companhia e objetivos do negócio."',
            'linkedin': 'https://www.linkedin.com/in/rha%C3%ADssa-manzini/',
            'imagem': 'images/rhaissa.png',  # URL da imagem do membro
        },
        {
            'nome': 'Myrella da Silva Pinto',
            'cargo': 'Scrum Master',
            'descricao': '"Atualmente estou em transição de carreira para a agilidade e, ajudar equipes a alcançar seu máximo potencial por meio da adoção das práticas ágeis se tornou uma paixão. Meu propósito é o de ser uma agente de transformação, criando soluções, gerando valor e, promovendo uma cultura de melhoria contínua dentro das equipes."',
            'linkedin': 'https://www.linkedin.com/in/mysilva/',
            'imagem': 'images/myrella.png',  # URL da imagem do membro
        },
    ]
    return render(request, 'equipe.html', {'membros': membros})