import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

matrix_a = [input().split() for _ in range(n)]
null = input()
matrix_b = [input().split() for _ in range(n)]

def summ_matrix_a_b(n,m,matrix_a1,matrix_b1):
    matrix_out = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix_out[i][j] = int(matrix_a1[i][j]) + int(matrix_b1[i][j])
    return matrix_out
    pass

for i in summ_matrix_a_b(n,m,matrix_a,matrix_b):
    print(*i)
 
###### v2 

