CREATE TABLE IF NOT EXISTS nobel_win(
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT,
    COUNT REAL
);

INSERT INTO nobel_win (YEAR,SUBJECT,WINNER,COUNTRY,CATEGORY,COUNT)
VALUES
    (1970,'Physics', 'Paul','France', 'Scientist',10),
    (1971,'Biology','Martin','USA', 'President', 11),
    (1981,'Physics', 'Peter', 'Russia', 'Scientist', 13);

SELECT COUNT AS 'TOTAL_COUNT'
FROM nobel_win
GROUP BY YEAR;

SELECT YEAR,SUM(COUNT) FROM nobel_win;

SELECT YEAR,SUBJECT FROM nobel_win
WHERE CATEGORY = 'Scientist'
ORDER BY YEAR DESC;