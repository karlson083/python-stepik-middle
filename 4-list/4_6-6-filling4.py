import os, math
clear = lambda: os.system('cls')
clear()

n  = int(input())

def create_matrix_filling(n1):
    matrix_out = []
    for i in range(n1):
        matrix_out.append([])
        for j in range(n1):
            if  (i <= j and i <= n1 - 1 - j) or (i >= j and i >= n1 - 1 - j):
                matrix_out[-1].append('1'.ljust(2))
            else:
                matrix_out[-1].append('0'.ljust(2))
    return matrix_out
    pass

for i in create_matrix_filling(n):
    print(*i)

 
###### v2
