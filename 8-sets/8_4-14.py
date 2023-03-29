import os, math
clear = lambda: os.system('cls')
clear()


s1 = '1930'
s2 = '2465748'

# s1, s2 = input(), input()

tmp_set = set(s1 + s2)

if len(tmp_set) == 10:
    print('YES')
else:
    print('NO')

###### v2


