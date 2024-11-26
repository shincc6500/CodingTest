-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE,'%Y-%m-%d')
from book b left join author a on b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY = '경제'
order by b.PUBLISHED_DATE asc
