n = [input() for _ in range(28)]
a = [0 for _ in range(31)]
answer = []
for i in n:
    a[int(i)] = 1

for index, value in enumerate(a):
    if index!=0 and value==0:
        answer.append(index)
answer.sort()
for p in answer:
    print(p)