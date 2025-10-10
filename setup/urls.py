from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from site_sintonize.views import index, politicas_privacidade, sondagem, sobre_nos, equipe, trilha, diagnostico, tratamento, burnout_survey_view, resultado_view,search_options, pomodoro, respiracao_guiada, analytics_dashboard, analytics_export, analytics_api

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
    path('respiracao_guiada/', respiracao_guiada, name='respiracao_guiada'),
    path('pomodoro/', pomodoro, name='pomodoro'),
    path('pomodoro.html', pomodoro, name='pomodoro_html'),  # Mantém compatibilidade com links antigos
    
    # URLs do painel de monitoramento
    path('analytics/', analytics_dashboard, name='analytics_dashboard'),
    path('analytics/export/', analytics_export, name='analytics_export'),
    path('analytics/api/', analytics_api, name='analytics_api'),
    
    # URLs de autenticação
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]