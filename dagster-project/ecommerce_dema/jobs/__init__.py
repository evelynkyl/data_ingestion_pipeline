from dagster import define_asset_job

from ..partitions import daily_partition


data_ingestion_key_selection = [
    "orders_data",
    "inventory_data",
    "order_inventory",
]

data_ingestion_job = define_asset_job(
    name="data_ingestion_job",
    selection=data_ingestion_key_selection,
    partitions_def=daily_partition,
)