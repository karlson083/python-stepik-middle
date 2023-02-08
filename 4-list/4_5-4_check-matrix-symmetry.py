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

def matrix_check_symmetry(input_matrix):
    matrix_simmetry = "YES"
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] != input_matrix[j][i]:
                matrix_simmetry = "NO"
                return matrix_simmetry
    return matrix_simmetry

print(matrix_check_symmetry(matrix_1))

###### v2

n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)