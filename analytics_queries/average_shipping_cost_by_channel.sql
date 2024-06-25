SELECT channel, AVG("shippingCost") AS avg_shipping_cost
FROM order_inventory
GROUP BY channel;