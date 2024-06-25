from dagster import Definitions, load_assets_from_modules
from dagster_dbt import dbt_cli_resource

from .assets import request_assets, dbt_assets
from .resources.csv_loader import CsvLoaderResource
from .resources.db_io_manager import db_io_manager
from .utils.constants import DBT_CONFIG, POSTGRES_CONFIG


def get_assets():
    all_assets = load_assets_from_modules(
        [request_assets, dbt_assets], group_name="dema_assets")
    return all_assets


def get_schedule():
    return None


def get_job():
    from .jobs import data_ingestion_job

    return [data_ingestion_job]


def get_resources():
    resources = {
        "csv_loader": CsvLoaderResource(),
        "dbt": dbt_cli_resource.configured(DBT_CONFIG),
        "db_io_manager": db_io_manager.configured(POSTGRES_CONFIG),
    }
    return resources


defs = Definitions(
    assets=get_assets(),
    schedules=get_schedule(),
    jobs=get_job(),
    resources=get_resources(),
)
