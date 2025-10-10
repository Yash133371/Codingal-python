CREATE TABLE IF NOT EXISTS SALESMAN (
    SM_ID TEXT PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    COMMISION REAL
);

INSERT INTO SALESMAN (SM_ID, NAME, CITY, COMMISION) VALUES
    ('1001', 'James', 'New York', 0.5),
    ('1002', 'John', 'Paris', 0.6),
    ('1003', 'Charlie', 'London', 0.4);

-- This is a comment it will be ignored by SQL

/*
This is a multiline comment
You can use it to disable code
*/

SELECT * FROM SALESMAN;

CREATE TABLE IF NOT EXISTS Orders (
    ORD_NO TEXT PRIMARY KEY,
    PR_AMT REAL,
    ORD_DATE TEXT,
    CST_ID TEXT,
    SM_ID TEXT
);

INSERT INTO Orders (ORD_NO, PR_AMT, ORD_DATE, CST_ID, SM_ID)
    ('70001', 100.5, '2025-10-10', '3001', '1001'),
    ('70002', 270.65, '2025-10-9', '3002', '1002'),
    ('70003', 230.11, '2025-10-8', '3003', '1003');

SELECT * FROM ORDERS;

SELECT NAME, COMMISION FROM SALESMAN;   