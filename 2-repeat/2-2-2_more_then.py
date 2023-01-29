import os, math
clear = lambda: os.system('cls')
clear()


s = input().split()
count = 0

for i in range(len(s)):
    s[i] = int(s[i])

for j in range(1,len(s)):
    if s[j] > s[j-1]:
        count += 1
print(count)


