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


def get_event_count(client, property_id, start_date, end_date, event_name):
    """Busca a contagem de um evento específico."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="eventName")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter={
            "filter": {
                "field_name": "eventName",
                "string_filter": {"value": event_name, "match_type": "EXACT"},
            }
        },
    )
    response = client.run_report(request)
    
    if response.rows:
        # Se houver linhas, o valor estará na primeira linha e primeira métrica
        return int(response.rows[0].metric_values[0].value)
    
    # Se não houver linhas, significa que o evento não ocorreu
    return 0


def format_report_data(response, dimension_key, metric_key, value_type=int):
    """Formata os dados do relatório em uma lista de dicionários."""
    data = []
    for row in response.rows:
        data.append({
            dimension_key: row.dimension_values[0].value,
            metric_key: value_type(row.metric_values[0].value)
        })
    return data


def get_form_abandonment_data(client, property_id, start_date, end_date):
    """
    Busca dados de visualização de perguntas do formulário para análise de abandono.
    Retorna uma lista ordenada de perguntas com suas visualizações.
    """
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="customEvent:event_label")  # Label das perguntas
        ],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter={
            "filter": {
                "field_name": "eventName",
                "string_filter": {
                    "value": "visualizacao_pergunta",
                    "match_type": "EXACT"
                },
            }
        },
    )

    response = client.run_report(request)

    # Processar dados
    perguntas_dict = {}
    for row in response.rows:
        label = row.dimension_values[0].value
        count = int(row.metric_values[0].value)

        # Extrair número da pergunta (ex: "Pergunta 1" -> 1)
        if "Pergunta" in label:
            try:
                numero = int(label.split()[-1])
                perguntas_dict[numero] = {
                    'pergunta': label,
                    'visualizacoes': count
                }
            except (ValueError, IndexError):
                pass

    # Ordenar por número da pergunta e retornar lista
    perguntas_ordenadas = []
    for i in range(1, 13):  # 12 perguntas
        if i in perguntas_dict:
            perguntas_ordenadas.append(perguntas_dict[i])
        else:
            # Se não houver dados para essa pergunta, adicionar com 0
            perguntas_ordenadas.append({
                'pergunta': f'Pergunta {i}',
                'visualizacoes': 0
            })

    return perguntas_ordenadas 