import os
from math import factorial as fact
clear = lambda: os.system('cls')
clear()


n = 3
#list_full = []
#n = int(input())

def tr_ps(n1,m1):
    return int(fact(n1) / (fact(m1) * fact(n1 - m1)))
    pass

for i in range(n):
    list1 = []
    for j in range(i+1):
        list1.append(tr_ps(i,j))
    print(*list1)
#    list_full.append(list1)

#print(*(*list_full), sep='\n')

###### v2
