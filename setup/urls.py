from django.contrib import admin
from django.urls import path, include
from site_sintonize.views import index, politicas_privacidade, sondagem, sobre_nos, equipe, trilha, diagnostico, tratamento, burnout_survey_view, resultado_view,search_options


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index.html', index, name='index'), 
    path('sondagem.html',sondagem, name='sondagem' ),
    path('politicas_privacidade', politicas_privacidade, name='politicas_privacidade'), 
    path('sobre_nos/', sobre_nos, name='sobre_nos'),
    path('equipe/', equipe, name='equipe'),
    path('trilha/', trilha, name='trilha'),
    path('diagnostico/', diagnostico, name='diagnostico'),
     path('tratamento/', tratamento, name='tratamento'),
    path('burnout-survey/', burnout_survey_view, name='burnout_survey'),
    path('resultado/<int:score>/', resultado_view, name='resultado'),
    path('search-options/', search_options, name='search_options'),
]