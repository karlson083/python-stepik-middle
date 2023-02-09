import os, math
clear = lambda: os.system('cls')
clear()

n = int(input())

def create_matrix_classic_n(n):
    matrix_out = [input().split() for _ in range(n)]
    for i in range(len(matrix_out)):
        for j in range(len(matrix_out[i])):
            matrix_out[i][j] = int(matrix_out[i][j])
    return matrix_out
    pass

matrix_1 = create_matrix_classic_n(n)

def check_number_line(input_matrix):
    list_from_matrix = []
    n = len(input_matrix)
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            list_from_matrix.append(input_matrix[i][j])
    list_from_matrix.sort()  
        
    return list_from_matrix == list(range(1,n ** 2 +1))

def check_sum_in_rows(input_matrix):
    for i in range(1,len(input_matrix)):
        if sum(input_matrix[0]) != sum(input_matrix[i]):
            return False
    return True

def check_diagonali(input_matrix):
    n = len(input_matrix)
    main_diagonal = 0
    second_diagonal = 0
    for i in range(n):
        main_diagonal += input_matrix[i][i]
        second_diagonal += input_matrix[n - i - 1][i]
    return main_diagonal == second_diagonal

def check_sum_in_col(input_matrix):
    n = len(input_matrix)
    matrix_tmp = []
    for i in range(n):
        matrix_tmp.append([])
        for j in range(n):
            matrix_tmp[-1].append(input_matrix[j][i])
    return check_sum_in_rows(matrix_tmp)

if check_number_line(matrix_1) and check_diagonali(matrix_1) and check_sum_in_rows(matrix_1) and check_sum_in_col(matrix_1):
    print('YES')
else:
    print('NO')

 
###### v2
