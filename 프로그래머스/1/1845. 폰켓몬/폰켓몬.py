def solution(nums):
    answer = 0
    N = len(nums)
    if N/2 <= len(set(nums)):
        answer = int(N/2)
    else:
        answer = len(set(nums))
    return answer