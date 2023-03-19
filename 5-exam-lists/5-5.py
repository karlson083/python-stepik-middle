import os
clear = lambda: os.system('cls')
clear()

q = int(input())

list_matrix = []
for _ in range(q):
    list_matrix.append(input().split())
    for i in range(len(list_matrix[-1])):
        list_matrix[-1][i] = int(list_matrix[-1][i])

res = 'YES'

for i in range(q):
    for j in range(q):
        if i != j:
            if list_matrix[i][j] != list_matrix[q-1-j][q-1-i]:
                res = 'NO'
                break
if list_matrix[0][0] != list_matrix[-1][-1]:
    res = 'NO'

print(res)

#-------------------- v2

