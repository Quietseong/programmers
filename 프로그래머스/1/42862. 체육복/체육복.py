#+test case
#lost = [2,4]
#reserve = [1,2,5]
#n=5

def solution(n, lost, reserve):
    lost_set = set(lost) #2,4
    reserve_set = set(reserve) #1,2,5
    dup = lost_set & reserve_set #2

    lost_set -= dup #4
    reserve_set -= dup #1,5

    for i in reserve_set: #여벌 전 후 idx의 도난 체육복 체크
        if i-1 in lost_set: #4
            lost_set -= {i-1, } #remove 4, remove():KeyErr
        elif i+1 in lost_set: #i-1에 없는 경우
            lost_set -= {i+1, } #remove

    return n - len(lost_set) #5-0=5