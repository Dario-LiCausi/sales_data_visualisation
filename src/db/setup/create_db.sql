CREATE TABLE IF NOT EXISTS sales (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    product VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    branch VARCHAR(100) NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL
);
