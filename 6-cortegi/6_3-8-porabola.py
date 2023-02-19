import os, math
clear = lambda: os.system('cls')
clear()

a, b, c = [int(input()) for _ in range(3)]

res = (-(b/(2*a)), (4 * a *c - b **2) / (4 * a))

print(res)


###### v2
