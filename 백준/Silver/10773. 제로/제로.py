import sys

K = int(sys.stdin.readline())

stack = []

for _ in range(K):
    value = int(sys.stdin.readline())

    if value == 0:
        stack.pop()

    else:
        stack.append(value)

print(sum(stack))