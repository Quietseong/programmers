def solution(n, times):
    answer = 0
    start, end = 1, min(times)*n #범위 지정, 근데 max도 되는데..?
    while start <= end:
        mid = (start+end)//2
        cnt = 0 # 입국심사받은 사람 수
        for time in times: #[7, 10]
            cnt += mid//time #mid=7 cnt=1
            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
            
    return answer