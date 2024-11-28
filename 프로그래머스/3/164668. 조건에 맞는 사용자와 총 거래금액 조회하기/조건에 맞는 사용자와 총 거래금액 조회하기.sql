-- 코드를 입력하세요
select U.USER_ID,U.NICKNAME, a.TOTAL_SALES
from USED_GOODS_USER u inner join 
(SELECT WRITER_ID, sum(price) as TOTAL_SALES
from USED_GOODS_BOARD
where STATUS = 'DONE'
group by WRITER_ID)a on u.USER_ID = a.WRITER_ID
having TOTAL_SALES >= 700000
order by TOTAL_SALES
