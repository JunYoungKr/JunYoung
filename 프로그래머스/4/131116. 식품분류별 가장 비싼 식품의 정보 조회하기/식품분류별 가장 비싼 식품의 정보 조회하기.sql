-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 식품 가격을 기준으로 내림차순

select CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME from food_product
where category in ('과자', '국', '김치', '식용유')
and price in(select max(price) from food_product group by category)
order by price DESC