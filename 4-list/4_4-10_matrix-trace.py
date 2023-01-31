import os
clear = lambda: os.system('cls')
clear()

q = int(input())

def create_matrix_traditional_input(q1):
    output_list_matrix = []
    for _ in range(q1):
        output_list_matrix.append(input().split())
    return output_list_matrix

def matrix_trace(matrix_input, q1):
    res = 0
    for i in range(q1):
        res += int(matrix_input[i][i])
    return res

print(matrix_trace(create_matrix_traditional_input(q),q))

###### v2


res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)