import os
clear = lambda: os.system('cls')
clear()

q = int(input())

def create_matrix_traditional_input(q1):
    output_list_matrix = []
    for _ in range(q1):
        output_list_matrix.append(input().split())
    return output_list_matrix

def count_more_medium(list_input):
    res = 0
    print(list_input)
    for i in range(len(list_input)):
        list_input[i] = int(list_input[i])
    for i in list_input:
        if i > sum(list_input) / len(list_input):
            res += 1
    return res

for i in create_matrix_traditional_input(q):
    print(count_more_medium(i))


###### v2


