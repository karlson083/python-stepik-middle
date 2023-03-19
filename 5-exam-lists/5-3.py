import os
clear = lambda: os.system('cls')
clear()

q = int(input())

list_matrix = []
for _ in range(q):
    list_matrix.append(input().split())
    for i in range(len(list_matrix[-1])):
        list_matrix[-1][i] = int(list_matrix[-1][i])


list_for_res = []

for i in range(q):
    list_for_res.append([])
    for j in range(q):
        list_for_res[-1].append(list_matrix[j][i])

for i in range(q):
    print(*list_for_res[i])


#-------------------- v2

n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)
