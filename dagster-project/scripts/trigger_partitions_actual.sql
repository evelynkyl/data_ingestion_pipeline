-- Create trigger to route inserts to correct partition for order_data
CREATE TRIGGER insert_order_data_trigger
BEFORE INSERT ON order_data
FOR EACH ROW EXECUTE FUNCTION insert_into_partitioned_table();

-- Create trigger to route inserts to correct partition for order_inventory
CREATE TRIGGER insert_order_inventory_trigger
BEFORE INSERT ON order_inventory
FOR EACH ROW EXECUTE FUNCTION insert_into_partitioned_table();
