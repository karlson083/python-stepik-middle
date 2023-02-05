import os
clear = lambda: os.system('cls')
clear()

n, m = int(input()), int(input())


for i in range(n):
    for j in range(m):
        print(str(i * j).ljust(3), end = '')
    print()

###### v2

