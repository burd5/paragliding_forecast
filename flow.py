from scripts.get_weather_forecast import get_weather_forecast
from utils import get_most_recent_data, add_data_to_azure_blob_storage
from prefect import flow, task

@task
def get_most_recent_forecast():
    pass

@task
def add_records_to_azure_blob_storage():
    pass

@flow
def update_weather_records():
    pass