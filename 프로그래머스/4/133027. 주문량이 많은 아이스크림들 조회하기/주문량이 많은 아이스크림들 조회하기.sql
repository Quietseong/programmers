# Tab: FIRST_HALF(PK: FLAVOR), JULY(PK: SHIPMENT_ID)
# JULY 테이블은 FALVOR가 흩어져 있음 -> group by 로 맛별로 모아두기
-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF F
    INNER JOIN(SELECT FLAVOR, SUM(TOTAL_ORDER) AS JULY_TOTAL_ORDER
               FROM JULY
               GROUP BY FLAVOR) J
    ON F.FLAVOR = J.FLAVOR
ORDER BY TOTAL_ORDER + JULY_TOTAL_ORDER DESC
LIMIT 3