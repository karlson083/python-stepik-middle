import os, math
clear = lambda: os.system('cls')
clear()


list_input = input().split()
set_out = set()
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
for i in list_input:
    if i in set_out:
        print('YES')    
    else:
        print('NO')
        set_out.add(i)


###### v2


numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)