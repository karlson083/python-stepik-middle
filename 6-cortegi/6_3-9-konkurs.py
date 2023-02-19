import os, math
clear = lambda: os.system('cls')
clear()

n = int(input())

list = [tuple(input().split()) for _ in range(n)]

for i in list:
    print(*i)

print()

for i in list:
    if i[-1] in ('4','5'):
        print(*i)



###### v2
