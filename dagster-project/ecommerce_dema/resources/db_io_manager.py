import pandas as pd

from dagster import IOManager, io_manager


class DbIOManager(IOManager):
    """IOManager to handle loading the contents of tables as pandas DataFrames.

    Does not handle cases where data is written to different schemas for different outputs, and
    uses the name of the asset key as the table name.
    """

    def __init__(self, con_string: str):
        self._con = con_string

    def handle_output(self, context, obj):
        if isinstance(obj, pd.DataFrame):
            table_name = context.asset_key.path[-1]
            try:
                obj.to_sql(name=table_name, con=self._con, if_exists="replace", index=False)
                context.add_output_metadata({"num_rows": len(obj), "table_name": table_name})
            except Exception as e:
                raise RuntimeError(f"Error writing DataFrame to database: {str(e)}")
        elif obj is None:
            # dbt has already written the data to this table
            pass
        else:
            raise ValueError(f"Unsupported object type {type(obj)} for DbIOManager.")


    def load_input(self, context) -> pd.DataFrame:
        """Load the contents of a table as a pandas DataFrame."""
        table_name = context.asset_key.path[-1]
        return pd.read_sql(f"SELECT * FROM {table_name}", con=self._con)


@io_manager(config_schema={"con_string": str})
def db_io_manager(context):
    return DbIOManager(context.resource_config["con_string"])
