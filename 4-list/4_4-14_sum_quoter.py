import os
clear = lambda: os.system('cls')
clear()

q = int(input())

def create_matrix_traditional_input(q1): # Заполняет квадратную матрицу/список из значений разделеных пробелом строк разделенных ентером
    output_list_matrix = []
    for _ in range(q1):
        output_list_matrix.append(input().split())
    return output_list_matrix



def sum_quotter(input_matrix, n): #Находит сумму четвертей матрицы без диагоналий
    list_n = []
    list_e = []
    list_s = []
    list_w = []


    for i in range(n):
        for j in range(n):
            if (i < j and i < (n - 1 - j)): #N
                list_n.append(int(input_matrix[i][j]))
            
            if (i < j and i > (n - 1 - j)): #E
                list_e.append(int(input_matrix[i][j]))

            if (i > j and i > (n - 1 - j)): #S
                list_s.append(int(input_matrix[i][j]))

            if (i > j and i < (n - 1 - j)): #W
                list_w.append(int(input_matrix[i][j]))
    
    print('Верхняя четверть:', sum(list_n))
    print('Правая четверть:', sum(list_e))
    print('Нижняя четверть:', sum(list_s))
    print('Левая четверть:', sum(list_w))
    pass
    

sum_quotter(create_matrix_traditional_input(q),q)



###### v2


n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0], 
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0], 
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])