-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.price*o.amount) as TOTAL_SALES
from FOOD_PRODUCT p left join FOOD_ORDER o on p.product_ID = o.product_Id
where o.PRODUCE_DATE like '2022-05%'
group by p.PRODUCT_NAME
order by 3 desc, p.PRODUCT_ID