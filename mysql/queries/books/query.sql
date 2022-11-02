SELECT * from users;

INSERT INTO users (name, created_at, updated_at)
VALUES ("Jane Amseden", NOW(), NOW()), ("Emily Dixon", NOW(), NOW()), ("Theodore Dostoevsky", NOW(), NOW()), ("William Shapiro", NOW(), NOW()), ("Lao Xiu", NOW(), NOW());

INSERT INTO books (title)
VALUES ("C Sharp"), ("Java"), ("Python"), ("PHP"), ("Ruby");

UPDATE books
SET title = "C#"
WHERE id = 1;

SELECT * from books;

UPDATE users
SET name = "Bill Shapiro"
WHERE id = 4;

INSERT INTO favorites (user_id, book_id)
VALUES (1,1), (1,2),
 (2,1), (2,2), (2,3),
 (3,1), (3,2), (3,3), (3,4),
 (4,1), (4,2), (4,3), (4,4), (4,5);

SELECT * FROM users
JOIN favorites ON users.id = favorites.user_id
WHERE favorites.book_id = 3;


SELECT * FROM favorites;
DELETE FROM favorites
WHERE user_id = 1 AND favorites.book_id = 3


INSERT INTO favorites (user_id, book_id)
VALUES (5,2)

SELECT * FROM favorites
WHERE user_id = 3;

SELECT * FROM favorites
WHERE book_id = 5