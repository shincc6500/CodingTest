WITH A AS (
SELECT PRODUCT_NAME
        ,PRICE
        ,CATEGORY
        ,RANK() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) FOOD_RANK
FROM FOOD_PRODUCT
)

SELECT CATEGORY
    ,PRICE MAX_PRICE
    ,PRODUCT_NAME
FROM A
WHERE FOOD_RANK = 1
AND CATEGORY IN ('과자','국','김치','식용유')
ORDER BY MAX_PRICE DESC