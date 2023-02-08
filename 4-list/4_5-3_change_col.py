import os
clear = lambda: os.system('cls')
clear()

n, m = int(input()), int(input())

def create_matrix_classic_n(n):
    matrix_out = []
    for _ in range(n):
        matrix_out.append(input().split())
    for i in range(len(matrix_out)):
        for j in range(len(matrix_out[i])):
            matrix_out[i][j] = int(matrix_out[i][j])
    return matrix_out
    pass

matrix_1 = create_matrix_classic_n(n)
matrix_change = create_matrix_classic_n(1)

matrix_out = []
for k in range(n):
    matrix_out.append([])
    for l in range(len(matrix_1[k])):
        if l == matrix_change[0][0]:
            matrix_out[-1].append(matrix_1[k][matrix_change[0][1]])
        elif l == matrix_change[0][1]:
            matrix_out[-1].append(matrix_1[k][matrix_change[0][0]])
        else:
            matrix_out[-1].append(matrix_1[k][l])
for m in matrix_out:
    print(*m)

###### v2

n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)