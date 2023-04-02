import os, math
clear = lambda: os.system('cls')
clear()


n = int(input())

list1 = [input() for _ in range(n)]

set1 = set(list1[0])

for i in range(1,n):
    set1 &= set(list1[i])



list_out = list(set1)
for i in range(len(list_out)):
    list_out[i] = int(list_out[i])


list_out.sort()
print(*list_out)

###### v2


n = int(input())
numbers = [input() for _ in range(n)]

num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))