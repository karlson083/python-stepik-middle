import os
clear = lambda: os.system('cls')
clear()

n, m = int(input()), int(input())

def create_matrix_classic_n(n):
    matrix_out = []
    for _ in range(n):
        matrix_out.append(input().split())
    for i in range(len(matrix_out)):
        for j in range(len(matrix_out[i])):
            matrix_out[i][j] = int(matrix_out[i][j])
    return matrix_out
    pass

def maximum_in_matrix_index(input_matrix):
    output_index = [0,0]
    max_tmp = input_matrix[0][0]
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] > max_tmp:
                max_tmp = input_matrix[i][j]
                output_index = [i,j]
    return output_index
    pass

print(*(maximum_in_matrix_index(create_matrix_classic_n(n))))

###### v2

