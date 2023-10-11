import os, math
clear = lambda: os.system('cls')
clear()

set1 = set('4 2 5 10 6 2'.split())
set2 = set("10 4 7 6 3 10".split())
set3 = set("1 2 1 5 9 5".split())

'''
set1 = set(input().split())
set2 = set(input().split())
set3 = set(input().split())
'''


set12 = set1 & set2

list_out = list(set12 - set3)

for i in range(len(list_out)):
    list_out[i] = int(list_out[i])

list_out.sort(reverse=True)

print(*list_out)

###### v2
