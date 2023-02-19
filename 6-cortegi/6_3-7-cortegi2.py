import os, math
clear = lambda: os.system('cls')
clear()

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
res = []
for i in numbers:
    res.append(sum(i) / len(i))

print(res)


###### v2
