# def solution(n, lost, reserve):
#     lost = set(lost) - set(reserve)
#     reserve = set(reserve) - set(lost)

#     for i in reserve:
#         if i-1 in lost:
#             lost -= {i-1, }
#         else:
#             lost -= {i+1, }
#     return n - len(lost)

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    reserve_and_lost = lost_set & reserve_set

    lost_set -= reserve_and_lost
    reserve_set -= reserve_and_lost

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set -= {i - 1, }
        elif i + 1 in lost_set:
            lost_set -= {i + 1, }

    return n - len(lost_set)    