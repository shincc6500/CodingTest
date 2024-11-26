-- 코드를 입력하세요
SELECT MCDP_CD as '진료과 코드', count(*) as '5월 예약 건수'
from APPOINTMENT
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by 2,1
