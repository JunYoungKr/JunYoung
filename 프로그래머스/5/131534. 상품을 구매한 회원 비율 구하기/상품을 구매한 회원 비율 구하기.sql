-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH, COUNT(DISTINCT A.USER_ID) AS PUCHASED_USERS, ROUND(COUNT(DISTINCT B.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1 ) AS PUCHASED_RATIO
FROM USER_INFO AS A
LEFT JOIN ONLINE_SALE AS B
ON A.USER_ID = B.USER_ID
WHERE A.JOINED LIKE '2021-%' AND B.SALES_DATE IS NOT NULL
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH
# 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율
# 2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수