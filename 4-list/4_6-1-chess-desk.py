import os, math
clear = lambda: os.system('cls')
clear()

nm  = input()

def create_chess_desk(n1,m1):
    matrix_out = []
    for i in range(n1):
        if not matrix_out:
            matrix_out.append(['.'])
        elif matrix_out[-1][0] == '.':
            matrix_out.append(['*'])
        elif matrix_out[-1][0] == '*':
            matrix_out.append(['.'])
                
        for j in range(1,m1):
            if  matrix_out[-1][-1] == '.':
                matrix_out[-1].append('*')
            elif matrix_out[-1][-1] == '*':
                matrix_out[-1].append('.')
        
            
    return matrix_out
    pass

for i in create_chess_desk(int(nm[0]),int(nm[-1])):
    print(*i)

 
###### v2
