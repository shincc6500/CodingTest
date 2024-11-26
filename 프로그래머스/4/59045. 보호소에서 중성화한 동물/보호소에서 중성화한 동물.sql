-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i left join ANIMAL_OUTS o on i.animal_ID = o.animal_ID
where i.sex_upon_INTAKE like '%INTACT%' and o.sex_upon_OUTCOME regexp('Spayed|NEUTERED')
order by i.ANIMAL_ID