SELECT
    "productId",
    COUNT(*) AS total_orders,
    SUM(o."quantity") AS total_quantity_sold
FROM order_inventory o
GROUP BY "productId"
ORDER BY total_quantity_sold DESC;
