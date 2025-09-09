"""
Context processors para o projeto Sintonize.
Fornece variáveis globais para todos os templates.
"""

from django.conf import settings


def google_analytics(request):
    """
    Context processor para Google Analytics.
    
    Fornece variáveis relacionadas ao Google Analytics para todos os templates,
    incluindo o ID de rastreamento e informações do ambiente.
    
    Args:
        request: HttpRequest object
        
    Returns:
        dict: Dicionário com variáveis do Google Analytics
    """
    return {
        'GA_MEASUREMENT_ID': getattr(settings, 'GA_MEASUREMENT_ID', 'G-BRR6F0VRZ7'),
        'ENVIRONMENT': getattr(settings, 'ENVIRONMENT', 'development'),
        'DEBUG_MODE': getattr(settings, 'DEBUG', True),
    }


def site_info(request):
    """
    Context processor para informações gerais do site.
    
    Args:
        request: HttpRequest object
        
    Returns:
        dict: Dicionário com informações do site
    """
    return {
        'SITE_NAME': 'Sintonize',
        'SITE_VERSION': '1.0.0',
        'CURRENT_URL': request.build_absolute_uri(),
        'IS_PRODUCTION': not getattr(settings, 'DEBUG', True),
    }
