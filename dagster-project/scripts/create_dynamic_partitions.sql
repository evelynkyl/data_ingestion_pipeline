CREATE OR REPLACE FUNCTION create_partition_for_table(table_name TEXT, date_value DATE) RETURNS VOID AS $$
DECLARE
    partition_name TEXT;
    start_date TIMESTAMP WITH TIME ZONE;
    end_date TIMESTAMP WITH TIME ZONE;
BEGIN
    IF table_name = 'order_data' THEN
        start_date := date_trunc('month', date_value);
        end_date := start_date + INTERVAL '1 month';
        partition_name := 'order_data_' || to_char(start_date, 'YYYY_MM');
    ELSIF table_name = 'order_inventory' THEN
        start_date := date_trunc('day', date_value);
        end_date := start_date + INTERVAL '1 day';
        partition_name := 'order_inventory_' || to_char(start_date, 'YYYY_MM_DD');
    ELSE
        RAISE EXCEPTION 'Table % does not support dynamic partitioning', table_name;
    END IF;

    -- Check if partition already exists
    IF NOT EXISTS(SELECT 1 FROM pg_tables WHERE tablename = partition_name) THEN
        EXECUTE format('
            CREATE TABLE %I (
                CHECK (dateTime >= TIMESTAMP WITH TIME ZONE %L AND dateTime < TIMESTAMP WITH TIME ZONE %L)
            ) INHERITS (%I);
        ', partition_name, start_date, end_date, table_name);
    END IF;
END;
$$ LANGUAGE plpgsql;
