CREATE TABLE IF NOT EXISTS salesman(
    sm_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commision TEXT
);

INSERT INTO salesman(sm_id,name,city,commision)
VALUES
    ("5001","James","New york","0.15"),
    ("5002","Nail","Paris","0.13"),
    ("5005","Alex","London","0.11"),
    ("5006","John","Rome","0.12"),
    ("5007","Paul","Paris","0.13");

CREATE TABLE IF NOT EXISTS customer(
    cust_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    sm_id
);

INSERT INTO customer(cust_id,cust_name,city,grade,sm_id) VALUES
    ("3001","Nick","New york","100","5001"),
    ("3002","Rick","New york","150","5001"),
    ("3004","David","Paris","175","5005"),
    ("3005","Julian","London","215","5007"),
    ("3006","Jake","new york","265","5002");

SELECT customer.cust_name, salesman.name, salesman.city
FROM customer
JOIN salesman ON customer.city = salesman.city;

SELECT customer.cust_name, salesman.name
FROM customer
JOIN salesman ON customer.sm_id = salesman.sm_id;