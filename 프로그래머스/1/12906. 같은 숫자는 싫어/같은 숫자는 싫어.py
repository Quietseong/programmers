def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #1. index사용, 이전 숫자와 비교하는 방법: 뒤에 따라나오는 숫자가 앞의 숫자와 동일하면 append하지 않음. 단, index가 0인 경우 주의
    # for i in range(len(arr)):
    #     if i==0 or arr[i-1] != arr[i]:
    #         answer.append(arr[i])
    # return answer
    #2. result로 비교, 인덱스가 아닌 뒤에 입력되는 숫자를 기준으로 입력된 숫자와 비교
    # for num in arr:
    #     if not answer or answer[-1] != num:
    #         answer.append(num)
    # return answer
    #3. 숫자 변수를 만들고 갱신하는 방법
    prev=None
    for cur in arr:
        if prev != cur:
            answer.append(cur)
        prev = cur
    return answer