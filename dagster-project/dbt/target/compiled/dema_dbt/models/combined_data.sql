select *
from "postgres_replica"."public"."orders_data" o
join "postgres_replica"."public"."inventory_data" i
    on i.productId = o.productId