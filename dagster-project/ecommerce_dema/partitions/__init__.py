from dagster import DailyPartitionsDefinition


daily_partition = DailyPartitionsDefinition(
    start_date="2024-02-01", end_offset=1
)
