import os, math
clear = lambda: os.system('cls')
clear()

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
res = 1
for i in numbers:
    res *= i
print(res)

###### v2