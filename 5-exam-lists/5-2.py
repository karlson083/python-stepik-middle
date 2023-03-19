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

for i in range(len(list_matrix)):
    for j in range(len(list_matrix[i])):
        if i >= q - 1 - j:
            list_for_res.append(list_matrix[i][j])

print(max(list_for_res))


