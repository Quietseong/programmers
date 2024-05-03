# TABLE: ECOLI_DATA
# 최초 대장균 개체의 PARENT_ID는 NULL
# 대장균 개체 100이하 low, 100~ 1000 medium, 1000 초과 high
# 대장균의 개체의 ID, 분류(SIZE) 출력
-- 코드를 작성해주세요
SELECT ID, IF(SIZE_OF_COLONY <= 100, 'LOW', IF(SIZE_OF_COLONY <= 1000, 'MEDIUM', 'HIGH')) AS SIZE
FROM ECOLI_DATA