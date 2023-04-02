import os, math
clear = lambda: os.system('cls')
clear()


set1 = set(input().split())
set2 = set(input().split())
set3 = list(set1 & set2)
for i in range(len(set3)):
    set3[i] = int(set3[i])
        
set3.sort()
print(*set3)

###### v2


set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())

print(*sorted(set1 & set2))