import os, math
clear = lambda: os.system('cls')
clear()


s = input().split()

for i in range(len(s)):
    s[i] = int(s[i])
for j in range(0, len(s) // 2):
    print(s[j * 2 + 1], s[j*2], sep = ' ', end = ' ')
if len(s) % 2:
    print(s[-1])




    ################## v2

digits = [int(c) for c in input().split()]

for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]
    
print(*digits)