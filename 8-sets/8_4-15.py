import os, math
clear = lambda: os.system('cls')
clear()


s1 = '327428'
s2 = '824723'

# s1, s2 = input(), input()

tmp_set1 = set(s1)
tmp_set2 = set(s2)

if tmp_set1 == tmp_set2:
    print('YES')
else:
    print('NO')

###### v2


