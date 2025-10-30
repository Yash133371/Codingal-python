CREATE TABLE IF NOT EXISTS nomnom (
    name TEXT,
    neighbourhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);

INSERT INTO nomnom (name, neighbourhood, cuisine, review,price,health) VALUES
    ('Peter','Brooklyn','Steak',4.4,'$$$$','A'),
    ('Jongro','Midtown','Korean',3.5,'$$','A'),
    ('Pocha','Midtown','Pizza',4,'$$$','B'),
    ('Lighthouse','Queens','Chinese',3.9,'$','A'),
    ('Minca','Downtown','Americian',4.6,'$$$','');

SELECT * FROM nomnom;

SELECT * from nomnom where cuisine = 'Chinese';

SELECT DISTINCT cuisine FROM nomnom;

SELECT * FROM nomnom WHERE review >= 4;

SELECT * FROM nomnom WHERE cuisine = 'Americian' AND price = '$$$';

SELECT * FROM nomnom WHERE neighbourhood = 'Midtown';

SELECT * FROM nomnom
WHERE neighbourhood IN ('Midtown', 'Downtown', 'Brooklyn');
