import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

def create_matrix_filling(n1,m1):
    matrix_out = []
    count = 0
    for _ in range(n1):
        matrix_out.append([])
        for _ in range(m1):
            count += 1
            matrix_out[-1].append(str(count).ljust(2))

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

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()