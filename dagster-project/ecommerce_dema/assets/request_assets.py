from typing import Callable

import pandas as pd
from dagster import (
    asset,
    Output,
    AssetCheckResult,
    AssetCheckSpec,
    MetadataValue,
)

from ..resources.csv_loader import CsvLoaderResource
from ..partitions import daily_partition


## Asset check / validation helper function
def count_nulls(df: pd.DataFrame, column: str) -> bool:
    # Returns True if there are null values in the specified column.
    return bool(df[column].isnull().sum() > 0)


## Actual assets
@asset(
    partitions_def=daily_partition,
    compute_kind="Python",
    output_required=False,
    io_manager_key="db_io_manager",
    check_specs=[
        AssetCheckSpec("non_null", asset="orders_data")]
)
def orders_data(csv_loader: CsvLoaderResource) -> Callable[[CsvLoaderResource], Output]:
    """
    Fetches orders data from a CSV file and saves it as its own table to Postgres database via IO manager
    """
    orders_url = (
        "https://dema-tech-assets.s3.eu-west-1.amazonaws.com/hiring-tests/orders.csv"
    )
    orders_df = csv_loader.load_csv_to_dataframe(orders_url)

    yield Output(
        orders_df,
        metadata={
            "preview": MetadataValue.md(orders_df.head().to_markdown()),
            "number_of_orders": len(orders_df) if orders_df is not None else 0,
        },
    )

    # Data check
    null_check = not count_nulls(orders_df, "orderId")
    yield AssetCheckResult(
        passed=null_check
    )

@asset(
    partitions_def=daily_partition,
    compute_kind="Python",
    output_required=False,
    io_manager_key="db_io_manager",
    check_specs=[AssetCheckSpec("non_null", asset="inventory_data")],
)
def inventory_data(csv_loader: CsvLoaderResource) -> Callable[[CsvLoaderResource], Output]:
    """Fetches inventory data from a CSV file and saves it as its own table to Postgres database via IO manager"""
    inventory_url = (
        "https://dema-tech-assets.s3.eu-west-1.amazonaws.com/hiring-tests/inventory.csv"
    )
    inventory_df = csv_loader.load_csv_to_dataframe(inventory_url)

    yield Output(
        inventory_df,
        metadata={
            "preview": MetadataValue.md(inventory_df.head().to_markdown()),
            "number_of_items_in_inventory": len(inventory_df)
            if inventory_df is not None
            else 0,
        },
    )

    # Data check
    null_check = not count_nulls(inventory_df, "productId")
    yield AssetCheckResult(
        passed=null_check
    )
