{{
    config(
        materialized='incremental',
        incremental_strategy='delete+insert',
        partition_by = {
            'field': '"dateTime"',
            'data_type': 'timestamp',
            'granularity': 'day'
       }
    )
}}


SELECT
    o.*,
	i.name AS inventory_name,
	i.quantity AS inventory_quantity,
	i.category AS inventory_category,
	i."subCategory" AS inventory_subCategory
FROM {{ source('dagster_db', 'orders_data') }} AS o
JOIN {{ source('dagster_db', 'inventory_data') }} AS i
    ON o."productId" = i."productId"
{% if is_incremental() %}
    WHERE o."dateTime" > (SELECT MAX(o2."dateTime") FROM {{ this }} o2)
{% endif %}