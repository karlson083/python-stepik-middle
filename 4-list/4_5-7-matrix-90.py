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



def print_matrix_90(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])-1,-1,-1):
            print(matrix[c][r], end=' ')
        print()

print_matrix_90(matrix_1)



###### v2

n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)