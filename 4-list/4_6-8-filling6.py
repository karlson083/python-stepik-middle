import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

def create_matrix_filling(n1,m1):
    matrix_out = []
    for i in range(n1):
        matrix_out.append([])
        for j in range(m1):
            matrix_out[-1].append(str(i * m + j + 1).ljust(2))

    for i in range(1,n1,2):
        matrix_out[i].reverse()

    return matrix_out
    pass

for i in create_matrix_filling(n,m):
    print(*i)

 
###### v2 
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()