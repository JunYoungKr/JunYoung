-- 코드를 입력하세요
SELECT AUTHOR.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, SUM(BOOK_SALES.SALES * BOOK.PRICE)  AS TOTAL_SALES
FROM BOOK AS BOOK
LEFT JOIN AUTHOR AS AUTHOR
ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
RIGHT JOIN BOOK_SALES AS BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE BOOK_SALES.SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY, AUTHOR_ID
# 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순
ORDER BY AUTHOR.AUTHOR_ID, BOOK.CATEGORY DESC