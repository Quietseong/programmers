n, a, d = map(int, input().split())
n_list = list(map(int, input().split()))

answer = sum(1 for x in n_list if x==a and (a:=a+d))

print(answer)