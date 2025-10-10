CREATE TABLE supplier (
    SND TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SND, SNAME, STATUS, CITY) VALUES 
    ('S1', 'Smith', 20, 'London'),
    ('S2', 'Jones', 10, 'Paris'),
    ('S3', 'Blake', 30, 'Paris');

SELECT * from supplier;