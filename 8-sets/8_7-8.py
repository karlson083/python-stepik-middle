import os, math
clear = lambda: os.system('cls')
clear()

set1 = set(input())
set2 = set(input())

print("NO" if set1.isdisjoint(set2) else "YES")

###### v2
