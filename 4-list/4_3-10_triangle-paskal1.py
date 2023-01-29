import os
from math import factorial as fact
clear = lambda: os.system('cls')
clear()


n = 30
#n = int(input())
list1 = []


def tr_ps(n1,m1):
    return int(fact(n1) / (fact(m1) * fact(n1 - m1)))
    pass

for i in range(n+1):
    list1.append(tr_ps(n,i))

print(list1)








###### v2
