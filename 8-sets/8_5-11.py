import os, math
clear = lambda: os.system('cls')
clear()


n = int(input())
list_input = [input() for _ in range(n)]

for i in list_input:
    print(len(set(i.lower())))


###### v2


