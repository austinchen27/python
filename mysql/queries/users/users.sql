-- Query 1

SELECT * FROM users;


INSERT INTO users (first_name, last_name, email)
VALUES ("Austin", "Chen", "austin@email.com"), ("John", "Ross", "john@email.com"), ("Jeffrey", "Aeschliman", "jeffrey@email.com"), ("Ciaran", "Voros", "ciaran@email.com");


SELECT email FROM users WHERE id = 1;


SELECT * FROM users
ORDER BY id DESC LIMIT 1;


UPDATE users.users SET
last_name = "Pancakes"
WHERE id = 3;


DELETE FROM users WHERE id = 2;


SELECT * FROM users
ORDER BY first_name


SELECT * FROM users
ORDER BY first_name DESC

