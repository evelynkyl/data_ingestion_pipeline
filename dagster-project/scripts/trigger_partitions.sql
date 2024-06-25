-- To route inserts to the correct partition
CREATE OR REPLACE FUNCTION insert_into_partitioned_table() RETURNS TRIGGER AS $$
BEGIN
    PERFORM create_partition_for_table(TG_TABLE_NAME::TEXT, NEW.dateTime::DATE);
    EXECUTE format('INSERT INTO %I VALUES ($1.*);', TG_TABLE_NAME) USING NEW;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
