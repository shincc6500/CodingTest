-- 코드를 입력하세요
select distinct c.CAR_ID,  COALESCE(b.ABALIABILITY, '대여 가능') as ABALIABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as c
    left join (SELECT CAR_ID, 
                case when '2022-10-16' between START_DATE and END_DATE then '대여중'
                else '대여 가능' end as ABALIABILITY
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where '2022-10-16' between START_DATE and END_DATE) b on c.CAR_ID = b.CAR_ID
order by CAR_ID desc
