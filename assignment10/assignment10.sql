CREATE TABLE IF NOT EXISTS books(
id SERIAL PRIMARY KEY,
title VARCHAR(100) UNIQUE NOT NULL,
author TEXT NOT NULL,
year_published INT 
);

INSERT INTO books(title,author,year_published)
VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
('1984', 'George Orwell', 1949),
('One Hundred Years of Solitude', 'Gabriel García Márquez', 1967),
('The Lord of the Rings', 'J.R.R. Tolkien', 1954)

SELECT * FROM books;

SELECT * FROM books WHERE author = 'George Orwell';

UPDATE books 
SET year_published = 1957
WHERE author = 'Harper Lee'

DELETE FROM books WHERE title = 'The Lord of the Rings'

CREATE TABLE borrower(
id SERIAL PRIMARY KEY,
book_id INT,
borrower_name TEXT NOT NULL,
-- book_title VARCHAR(100) NOT NULL,
date_borrowed DATE DEFAULT CURRENT_DATE,
return_date DATE,
FOREIGN KEY(book_id) REFERENCES books(id)
);

INSERT INTO borrower(book_id,borrower_name,return_date)
VALUES
(2, 'Duke Luke', '2025-03-27'),
(3, 'Yaw Ming', '2023-07-07'),
(1, 'Shaq Quille', '2024-12-27')
-- DROP TABLE borrower

SELECT * FROM borrower

