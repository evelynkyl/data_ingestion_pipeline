SELECT AVG(o."amount" * o."quantity") AS average_order_value
FROM order_inventory o;
