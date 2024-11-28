-- 코드를 입력하세요
SELECT distinct(c.CAR_ID)
from CAR_RENTAL_COMPANY_CAR c left join CAR_RENTAL_COMPANY_RENTAL_HISTORY r on c.CAR_ID = r.CAR_ID
where CAR_TYPE = '세단' and history_id is not null and r.start_date like '%-10-%'
order by c.CAR_ID desc