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