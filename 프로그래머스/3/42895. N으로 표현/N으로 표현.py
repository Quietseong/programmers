def solution(N, number):
    answer = -1
    if number == N:
        return 1
    dp = [set() for i in range(8)] #최대 8개까지, dp[1]= N 한 개 조합, dp[2]= N 두 개 조합
    #case1: 단일 숫자 조합(5 55 555 5555)
    for i in range(len(dp)):
        dp[i].add(int(str(N)*(i+1)))
    #case2: 사칙연산 조합, dp[i]는 dp[i-1], dp[i-2]... dp[0]에 저장된 숫자로 조합 가능
    for i in range(1, 8): #if i =1
        for j in range(i): #j=0 
            for op1 in dp[j]: #dp[1]=5+5, 5-5, 5*5, 5//5, dp[2]=5+5+5, 5-5+5, 5-5*5..
                for op2 in dp[i-j-1]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2 != 0: #나눌때는 연산자가 0이 되면 안됨dp[i].add(op1//op2)
                        dp[i].add(op1//op2)
        if number in dp[i]:
            answer = i+1 #dp[1]에서 number가 발견된다면, 최소 2개 조합으로 완성되었기 때문
            break
    return answer
