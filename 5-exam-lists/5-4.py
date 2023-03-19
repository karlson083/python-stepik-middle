import os
clear = lambda: os.system('cls')
clear()

q = int(input())

list_matrix = [['.'] * q for _ in range(q)]

for i in range(len(list_matrix)):
    for j in range(len(list_matrix[i])):
        if i == j or i == q - j - 1 or j * 2  == q - 1 or i * 2  == q - 1:
            list_matrix[i][j] = '*'


for row in list_matrix:
    print(*row)


#-------------------- v2

