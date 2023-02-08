import os
clear = lambda: os.system('cls')
clear()

n = int(input())

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

matrix_1.reverse()

def print_matrix_rows(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')
        print()

print_matrix_rows(matrix_1)



###### v2
