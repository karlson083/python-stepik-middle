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
            matrix_out[-1].append('N')
        elif (x - j) * (y - i) == 2 or (x - j) * (y - i) == -2:
            matrix_out[-1].append('*')
        else:
            matrix_out[-1].append('.')
for k in matrix_out:
    print(*k)




 
###### v2

x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'
        
for row in board:
    print(*row)