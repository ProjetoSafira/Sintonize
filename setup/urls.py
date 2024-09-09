from django.contrib import admin
from django.urls import path, include
from site_sintonize.views import index, politicas_privacidade, sondagem


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index.html', index, name='index'), 
    path('sondagem.html',sondagem, name='sondagem' ),
    path('politicas_privacidade', politicas_privacidade, name='politicas_privacidade'), 
]
