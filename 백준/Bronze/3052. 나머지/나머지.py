n = [int(input()) for _ in range(10)]
B = 42
remain = []
for i in range(len(n)):
    remain.append(n[i]%B)

print(len(set(remain)))