import os, math
clear = lambda: os.system('cls')
clear()


s = '12345678910'

# s = input()

tmp_set = set(s)

if len(s) == len(tmp_set):
    print('YES')
else:
    print('NO')

###### v2


