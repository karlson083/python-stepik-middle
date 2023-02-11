import os, math
clear = lambda: os.system('cls')
clear()

n = int(input())

def create_matrix_filling(n1):
    matrix_out = [['0'.ljust(2)] * n1 for _ in range(n1)]
    for i in range(n1):
        matrix_out[i][i] = str('1'.ljust(2))
        matrix_out[n1-1-i][i] = str('1'.ljust(2))
    return matrix_out
    pass


for i in create_matrix_filling(n):
    print(*i)

 
###### v2
