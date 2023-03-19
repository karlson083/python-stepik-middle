import os
clear = lambda: os.system('cls')
clear()

list_in = 'a b c d e f g h i j k l m n'.split()
n = 3

list_in = input().split()
n = int(input())
list_out = [[] for _ in range(n)]
for i in range(len(list_in)):
    list_out[i % n].append(list_in[i])
print(list_out)