-- 코드를 입력하세요
# SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS COUNT
# FROM ANIMAL_OUTS
# WHERE HOUR(DATETIME) BETWEEN '0' and '23'
# GROUP BY HOUR
# ORDER BY HOUR

SET @HOUR = -1;
SELECT @HOUR := @HOUR + 1 AS HOUR,
    (SELECT COUNT(*)
    FROM ANIMAL_OUTS
    WHERE @HOUR = HOUR(DATETIME)) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
    