s = input()
check = [-1] * 26

for i in range(len(s)):
    index = ord(s[i]) - ord('a') #s[0] = 'b', index = 1(b를 의미)
    if check[index] == -1:
        check[index] = i

for i in range(26):
    print(check[i], end=" ")
    