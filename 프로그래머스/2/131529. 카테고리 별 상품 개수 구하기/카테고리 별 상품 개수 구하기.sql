-- 코드를 입력하세요
SELECT SUBSTRING(product_code,1,2) as CATEGORY,count(*) as PRODUCTS
from product
group by 1