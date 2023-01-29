import os, math
clear = lambda: os.system('cls')
clear()

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for st in list1:
    if max(st) > maximum:
        maximum = max(st)


print(maximum)
###### v2
