from django.urls import path
from main import views


urlpatterns = [
    path('', views.home_view, name ='home'),
    path('escolha1/', views.escolha1_view, name ='escolha1'),
    path('escolha2/', views.escolha2_view, name = 'escolha2'),
    path('escolha3/', views.escolha3_view, name = 'escolha3'),
    path('escolha4/', views.escolha4_view, name = 'escolha4'),
    path('resultado/', views.resultado_view, name='resultado'),
     path('sondagem/', views.sondagem, name='sondagem')
]
