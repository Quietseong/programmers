# TABLE: ECOLI_DATA
# ID, GENOTYPE, PARENT_GENOTYPE
# ID ASC
# CONV() 나 WHERE & 사용
# 부모의 형질을 모두 보유한 개체를 출력해야 함
# CHILD.ECOLI_DATA의 CHILD.PARENT_ID는 PARENT.PARENT_ID 형질(GENOTYPE을 이진수로)중 하나를 보유해야함(PARENT<CHILD)
# ID ASC
# EX) CHILD TABLE, ID8 인 경우 PARENT_ID는 6, GENOTYPE 13 -> 1101(1, 3, 4) 형질 보유 / PARENT.ID가 6의 형질은 5 -> 0101(1, 3) 
-- 코드를 작성해주세요
SELECT CHILD.ID, CHILD.GENOTYPE, PARENT.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA CHILD
LEFT JOIN ECOLI_DATA PARENT ON CHILD.PARENT_ID = PARENT.ID
WHERE PARENT.GENOTYPE & CHILD.GENOTYPE = PARENT.GENOTYPE 
# 부모 형질이 0101 & 자식 형질이 1101이면 0101이 됨. 이 연산 결과가 부모의 형질과 동일한 경우 TRUE 반환. 
# 즉, 부모의 형질이 자식에게도 동일하게 존재하는 모든 데이터를 선택
ORDER BY CHILD.ID ASC