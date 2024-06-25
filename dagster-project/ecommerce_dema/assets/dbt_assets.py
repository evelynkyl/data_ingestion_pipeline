from dagster_dbt import load_assets_from_dbt_project

from ..utils.constants import DBT_PROJECT_DIR, DBT_PROFILES_DIR


dbt_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR, DBT_PROFILES_DIR, io_manager_key="db_io_manager"
)
