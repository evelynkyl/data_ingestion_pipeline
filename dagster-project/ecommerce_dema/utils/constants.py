import os

from dotenv import load_dotenv
from dagster_postgres.utils import get_conn_string

from dagster._utils import file_relative_path


load_dotenv(dotenv_path='dagster.env')


PG_SOURCE_CONFIG = {
    "username": os.environ.get("DAGSTER_POSTGRES_USER"),
    "password": os.environ.get("DAGSTER_POSTGRES_PASSWORD"),
    "host": os.environ.get("DAGSTER_POSTGRES_HOST"),
    "port": os.environ.get("DAGSTER_POSTGRES_PORT"),
    "database": os.environ.get("POSTGRES_SOURCE_DATABASE"),
}
PG_DESTINATION_CONFIG = {
    "username": os.environ.get("DAGSTER_POSTGRES_USER"),
    "password": os.environ.get("DAGSTER_POSTGRES_PASSWORD"),
    "host": os.environ.get("DAGSTER_POSTGRES_HOST"),
    "port": os.environ.get("DAGSTER_POSTGRES_PORT"),
    "database": os.environ.get("POSTGRES_DB"),
}

POSTGRES_CONFIG = {
    "con_string": get_conn_string(
        username=PG_DESTINATION_CONFIG["username"],
        password=PG_DESTINATION_CONFIG["password"],
        hostname=PG_DESTINATION_CONFIG["host"],
        port=str(PG_DESTINATION_CONFIG["port"]),
        db_name=PG_DESTINATION_CONFIG["database"],
    )
}

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../dbt")
DBT_CONFIG = {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}
