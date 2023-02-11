import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

def create_matrix_filling(n1,m1):
    matrix_out = [[0] * m1 for _ in range(n1)]
    count = 0
    for i in range(m1):
        for j in range(n1):
            count += 1
            matrix_out[j][i] = str(count).ljust(2)

    return matrix_out
    pass


for i in create_matrix_filling(n,m):
    print(*i)

 
###### v2

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()