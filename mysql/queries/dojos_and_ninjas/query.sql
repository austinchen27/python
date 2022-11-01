SELECT * FROM dojos;

INSERT INTO dojos (name)
VALUES ("Austin's Dojo"), ("John's Dojo"), ("Jeffrey's Dojo")


SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja1", "A1", 77, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja11", "A11", 77, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja111", "A111", 77, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja2", "A2", 88, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja22", "A22", 88, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja222", "A222", 88, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja3", "A3", 88, 6);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja33", "A33", 88, 6);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Ninja333", "A333", 88, 6);

SELECT * FROM ninjas
WHERE id = 4;

SELECT * FROM ninjas
ORDER BY dojo_id ASC;

SELECT * FROM ninjas
ORDER BY dojo_id DESC;

SELECT * FROM 