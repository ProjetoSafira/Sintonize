"""
Middleware para registrar todos os acessos ao site
Use para gerar relatórios quando não tem acesso aos logs do servidor
"""

import logging
from django.utils import timezone

logger = logging.getLogger('access_log')

class AccessLogMiddleware:
    """
    Middleware que registra cada acesso ao site
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capturar dados antes da requisição
        timestamp = timezone.now()
        ip = self.get_client_ip(request)
        method = request.method
        path = request.path
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        referer = request.META.get('HTTP_REFERER', '')

        # Processar a requisição
        response = self.get_response(request)

        # Registrar o acesso
        logger.info(
            f'{ip} - [{timestamp.strftime("%d/%b/%Y:%H:%M:%S")}] '
            f'"{method} {path}" {response.status_code} '
            f'"{referer}" "{user_agent}"'
        )

        return response

    def get_client_ip(self, request):
        """Obter o IP real do cliente (mesmo atrás de proxy)"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
