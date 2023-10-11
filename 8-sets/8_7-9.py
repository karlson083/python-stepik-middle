import os, math
clear = lambda: os.system('cls')
clear()

set1 = set(input())
set2 = set(input())

print("YES" if  set2.issubset(set1) else 'NO')

###### v2
