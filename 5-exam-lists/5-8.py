import os
clear = lambda: os.system('cls')
clear()

n = int(input())

output_res = []
for i in range(n):
    output_res.append([])
    for j in range(n):
        output_res[-1].append(abs(i-j))

for row in output_res:
    print(*row)


#-------------------- v2
n = int(input())
arr = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in arr:
    print(*row)