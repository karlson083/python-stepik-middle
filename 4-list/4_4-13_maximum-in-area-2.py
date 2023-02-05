import os
clear = lambda: os.system('cls')
clear()

q = int(input())

def create_matrix_traditional_input(q1): # Заполняет квадратную матрицу/список из значений разделеных пробелом строк разделенных ентером
    output_list_matrix = []
    for _ in range(q1):
        output_list_matrix.append(input().split())
    return output_list_matrix



def max_in_area_opposite_quotter(input_matrix, q1): #Находит максимальное число области четвертей матрицы напротив друг друга
    list_tmp =[]
    for i in range(q1):
        for j in range(q1):
            if i == j or i+1 == ((j-q1)  * -1) or (i > j and i < (q1-1-j)) or (i<j and i> (q1-1-j)):
                list_tmp.append(int(input_matrix[i][j]))
    return max(list_tmp)

print(max_in_area_opposite_quotter(create_matrix_traditional_input(q),q))





###### v2

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                
print(largest)
