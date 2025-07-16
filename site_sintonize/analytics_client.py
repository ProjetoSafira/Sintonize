import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    RunRealtimeReportRequest,
)
from google.oauth2 import service_account
from datetime import datetime, timedelta

# Configurações do Google Analytics
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'setup', 'sintonize-analytics-credentials.json')
# IMPORTANTE: Substitua 'SEU_PROPERTY_ID' pelo ID numérico da sua propriedade do Google Analytics 4.
PROPERTY_ID = '495597072' 

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
    """Busca o número de usuários ativos em tempo real."""
    request = RunRealtimeReportRequest(
        property=f"properties/{property_id}",
        metrics=[Metric(name="activeUsers")],
    )
    response = client.run_realtime_report(request)
    
    total_active_users = 0
    if response.rows:
        # A resposta de tempo real pode ter vários valores, somamos todos
        for row in response.rows:
            metric_value = row.metric_values[0].value
            if metric_value.isdigit():
                total_active_users += int(metric_value)
                
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