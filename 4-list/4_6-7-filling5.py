import os, math
clear = lambda: os.system('cls')
clear()

n, m = [int(i) for i in input().split()]

def create_matrix_filling(n1,m1):
    matrix_out = []
    for i in range(n1):
        matrix_out.append([])
        for j in range(m1):
            matrix_out[-1].append(str((i + j) % m1 + 1).ljust(2))
            
    return matrix_out
    pass

for i in create_matrix_filling(n,m):
    print(*i)

 
###### v2 (i + j + 1) % m
