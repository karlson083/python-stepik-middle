import os
clear = lambda: os.system('cls')
clear()

q = int(input())
e = [i for i in range(1, q+1)]
list_matrix = []
for _ in range(q):
    list_matrix.append(input().split())
    for i in range(len(list_matrix[-1])):
        list_matrix[-1][i] = int(list_matrix[-1][i])

res = 'YES'


list_for_check = []


for i in list_matrix:
    list_for_check.append(list(set(i)))

for i in range(q):
    list_for_check.append([])
    for j in range(q):
        list_for_check[-1].append(list_matrix[j][i])
    list_for_check[-1] = list(set(list_for_check[-1]))

for i in list_for_check:
    if i != e:
        res = 'NO'
        break

print(res)

#-------------------- v2

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break
        
print(result)