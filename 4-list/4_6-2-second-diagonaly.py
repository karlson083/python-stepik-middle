import os, math
clear = lambda: os.system('cls')
clear()

n  = int(input())

def create_matrix_with_diagonaly(n1):
    matrix_out = []
    for i in range(n1):
        matrix_out.append([])
        for j in range(0,n1):
            if  i + j == n1 - 1:
                matrix_out[-1].append(1)
            elif i + j >= n1:
                matrix_out[-1].append(2)
            else:
                matrix_out[-1].append(0)
    return matrix_out
    pass

for i in create_matrix_with_diagonaly(n):
    print(*i)

 
###### v2
