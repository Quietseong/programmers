# 세 각 입력(3 input)
# 세 각의 합이 180 and 두 각이 같으면 isosceles
# 세 각의 합이 180 and 같은 각이 없으면 Scalene
# 세 각의 합이 180이 아닌 경우 Error

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

if a & b & c == 60:
    print('Equilateral')
elif a+b+c == 180:
    if a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')