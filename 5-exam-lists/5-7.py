import os
clear = lambda: os.system('cls')
clear()

xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])

matrix_out = []
for i in range(8):
    matrix_out.append([])
    for j in range(8):
        if i == y and j == x:
            matrix_out[-1].append('Q')
        elif abs(y - i) == abs(x - j) or x == j or y == i:
            matrix_out[-1].append('*')
        else:
            matrix_out[-1].append('.')
for k in matrix_out:
    print(*k)

#-------------------- v2
