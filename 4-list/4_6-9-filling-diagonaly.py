import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

def create_matrix_filling_deagonali(n1,m1):
    matrix_out = [['0'.ljust(2)] * m1 for _ in range(n1)]
    cnt = 1
    for q in range(n1 + m1 -1):
        for i in range(n1):
            for j in range(m1):
                if i + j == q:
                    matrix_out[i][j] = str(cnt).ljust(2)
                    cnt += 1

    return matrix_out
    pass

for i in create_matrix_filling_deagonali(n,m):
    print(*i)
 
###### v2 
