CREATE TABLE inventory_data (
    productId VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    quantity INTEGER,
    category VARCHAR(50),
    subCategory VARCHAR(50)
);

CREATE TABLE order_data (
    orderId UUID PRIMARY KEY,
    productId VARCHAR(50),
    currency VARCHAR(10),
    quantity INTEGER,
    shippingCost NUMERIC,
    amount NUMERIC,
    channel VARCHAR(50),
    channelGroup VARCHAR(50),
    campaign VARCHAR(50),
    dateTime TIMESTAMP WITH TIME ZONE
);

CREATE TABLE order_inventory (
    orderId UUID,
    productId VARCHAR(50),
    name VARCHAR(100),
    quantity INTEGER,
    category VARCHAR(50),
    subCategory VARCHAR(50),
    currency VARCHAR(10),
    order_quantity INTEGER,
    shippingCost NUMERIC,
    amount NUMERIC,
    channel VARCHAR(50),
    channelGroup VARCHAR(50),
    campaign VARCHAR(50),
    dateTime TIMESTAMP WITH TIME ZONE
);
