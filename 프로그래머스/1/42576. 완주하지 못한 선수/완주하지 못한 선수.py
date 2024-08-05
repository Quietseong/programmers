from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    answer = p-c
    return ''.join(list(answer))