CREATE TABLE IF NOT EXISTS nobel_win(
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
);

INSERT INTO nobel_win (YEAR,SUBJECT,WINNER,COUNTRY,CATEGORY)
VALUES
    (1970,'Physics', 'Paul','France', 'Scientist'),
    (1971,'Biology','Martin','USA', 'President'),
    (1981,'Physics', 'Peter', 'Russia', 'Scientist');

SELECT * FROM nobel_win
WHERE SUBJECT NOT LIKE 'P%';