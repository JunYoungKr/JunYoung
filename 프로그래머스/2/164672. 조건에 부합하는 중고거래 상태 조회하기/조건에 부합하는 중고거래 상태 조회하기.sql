-- 코드를 입력하세요
SELECT A.BOARD_ID, A.WRITER_ID, A.TITLE, A.PRICE,
CASE 
     WHEN A.STATUS = 'DONE' THEN '거래완료'
     WHEN A.STATUS = 'SALE' THEN '판매중'
     WHEN A.STATUS = 'RESERVED' THEN '예약중'
     ELSE '상태미정' -- 이 부분은 상태가 'DONE', 'SALE', 'RESERVED' 이외의 값을 가질 때 사용됩니다.
END AS STATUS
FROM USED_GOODS_BOARD AS A
WHERE A.CREATED_DATE = '2022-10-05' -- 정확한 날짜 매칭을 위해 '=' 사용
ORDER BY A.BOARD_ID DESC;
