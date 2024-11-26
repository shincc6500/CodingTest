-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(o.SALES_AMOUNT*p.PRICE) as SALES
from PRODUCT p left join OFFLINE_SALE o on p.product_id = o.product_id
group by 1
order by 2 desc,1