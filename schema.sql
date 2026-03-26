CREATE DATABASE food_waste_db;
USE food_waste_db;

CREATE TABLE food_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE daily_preparation (
    prep_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    date DATE,
    quantity_prepared FLOAT CHECK (quantity_prepared >= 0),
    FOREIGN KEY (item_id) REFERENCES food_items(item_id)
);

CREATE TABLE daily_consumption (
    cons_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    date DATE,
    quantity_consumed FLOAT CHECK (quantity_consumed >= 0),
    FOREIGN KEY (item_id) REFERENCES food_items(item_id)
);

CREATE TABLE waste_log (
    waste_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    date DATE,
    waste_quantity FLOAT,
    FOREIGN KEY (item_id) REFERENCES food_items(item_id)
);

CREATE TABLE alerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    date DATE,
    message VARCHAR(255),
    FOREIGN KEY (item_id) REFERENCES food_items(item_id)
);