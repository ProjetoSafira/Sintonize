import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from google.oauth2 import service_account
from datetime import datetime, timedelta

# Configurações do Google Analytics
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'setup', 'sintonize-analytics-credentials.json')
PROPERTY_ID = 'G-BRR6F0VRZ7'.split('-')[-1] # Extrai o ID numérico

def get_analytics_client():
    """Cria um cliente autenticado para a API do Google Analytics."""
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return BetaAnalyticsDataClient(credentials=credentials)

def get_report(client, property_id, start_date, end_date, dimensions, metrics):
    """Executa uma consulta na API do Google Analytics."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=dimensions,
        metrics=metrics,
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    return client.run_report(request)

def get_active_users(client, property_id):
    """Busca o número de usuários ativos nos últimos 5 minutos."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="unifiedScreenName")], # ou pagePath
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="5minutesAgo", end_date="today")],
    )
    response = client.run_report(request)
    total_active_users = 0
    if response.rows:
        for row in response.rows:
            total_active_users += int(row.metric_values[0].value)
    return total_active_users

def format_report_data(response, dimension_key, metric_key, value_type=int):
    """Formata os dados do relatório em uma lista de dicionários."""
    data = []
    for row in response.rows:
        data.append({
            dimension_key: row.dimension_values[0].value,
            metric_key: value_type(row.metric_values[0].value)
        })
    return data 