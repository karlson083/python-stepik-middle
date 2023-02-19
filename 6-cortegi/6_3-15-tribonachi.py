import os, math
clear = lambda: os.system('cls')
clear()

n = int(input())

res = []
for _ in range(n):
    if len(res) < 3:
        res.append(1)
    else:
        res.append(sum(res[-3:]))

print(*res)


###### v2
