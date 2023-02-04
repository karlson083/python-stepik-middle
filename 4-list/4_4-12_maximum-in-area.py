import os
clear = lambda: os.system('cls')
clear()

q = int(input())

def create_matrix_traditional_input(q1): # Заполняет квадратную матрицу/список из значений разделеных пробелом строк разделенных ентером
    output_list_matrix = []
    for _ in range(q1):
        output_list_matrix.append(input().split())
    return output_list_matrix



def max_in_area(input_matrix, q1): #Находит максимальное число области матрицы
    list_tmp =[]
    for i in range(len(input_matrix)):
        for j in range(i+1):
            list_tmp.append(int(input_matrix[i][j]))
    print(list_tmp)
    #return max(list_tmp)


max_in_area(create_matrix_traditional_input(q),q)
#print(max_in_area(create_matrix_traditional_input(q),q))





###### v2


