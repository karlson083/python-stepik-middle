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

def change_diagonaly(input_matrix):
    for i in range(len(input_matrix) * -1, 0):
        input_matrix[i][i], input_matrix[(i+1) * -1][i] = input_matrix[(i+1) * -1][i], input_matrix[i][i]

    return input_matrix

def print_matrix_rows(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')
        print()

print_matrix_rows(change_diagonaly(matrix_1))



###### v2
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)