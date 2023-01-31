import os
clear = lambda: os.system('cls')
clear()

n, m = int(input()), int(input())
start_list =[]

def create_matrix_from_list(input_list, n1, m1):
    output_list = []
    cnt = 0
    for _ in range(n1):
        output_list.append([input_list[cnt]])
        cnt += 1
        for _ in range(m1-1):
            output_list[-1].append(input_list[cnt])
            cnt += 1
    return output_list

def input_list_with_enter(count):
    output_list = []
    for _ in range(count):
        output_list.append(input())
    return output_list

def print_matrix_rows(matrix, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c], end=' ')
        print()

def print_matrix_cols(matrix, rows, cols):
    for c in range(cols):
        for r in range(rows):
            print(matrix[r][c], end=' ')
        print()


print_matrix_rows(create_matrix_from_list(input_list_with_enter(n*m) ,n ,m), n, m)

###### v2


