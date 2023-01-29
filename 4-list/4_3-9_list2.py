import os, math
clear = lambda: os.system('cls')
clear()


n = 3
#n = int(input())
list1 = []

for i in range(1,n+1):
    list1.append(list(range(1,i+1)))
'''
for row in list1:
    print(row)
'''
print(*list1, sep='\n')





###### v2
