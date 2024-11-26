-- 코드를 입력하세요
SELECT b.CATEGORY, sum(s.SALES) as TOTAL_SALES
from book b left join book_sales s on b.BOOK_ID = s.BOOK_ID
where s.SALES_DATE like '2022-01%'
group by b.CATEGORY
order by 1