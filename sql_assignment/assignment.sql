
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
    -- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Product (product_name, category, price)
VALUES 
    ('HP ENVY x360', 'Laptops', 4200.00),
    ('Anker Powerbank', 'Accessories', 500.00),
    ('Beats Solo', 'Headphones', 2000.00),
    ('Silicon case', 'Accessories', 350.00),
    ('FitPro Watch', 'Smart Watches', 2270.00);


CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,
    -- product_id INT REFERENCES Product (id),
    product_id VARCHAR(10) UNIQUE,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10,20),
    -- total_price DECIMAL(quantity_sold * product(price))
);

INSERT INTO Sales (product_id, quantity_sold, sale_date, total_price) 
VALUES
('PC002', 20, '2025-05-05', 75.00),
('ACS034', 3, '2025-09-35', 100.00),
('HP020', 13, '2025-07-24', 200.00),
('APL001', 1, '2025-01-12', 10.00),
('SW006', 18, '2025-12-13', 56.00);


SELECT * FROM Product

SELECT product_name, price FROM Product

SELECT * FROM product LIMIT 2

SELECT total_price FROM Sales WHERE total_price > 100

SELCT * FROM product 
WHERE category = 'Accessories',

SELECT count(*) AS product_name
FROM product;

SELECT SUM(total_price)
FROM sales;

SELECT avg(price)
FROM product;


