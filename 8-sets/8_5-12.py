import os, math
clear = lambda: os.system('cls')
clear()


n = int(input())
i = ''
for _ in range(n):
    i += input()
print(len(set(i.lower())))


###### v2

n = int(input())
symbols = set()

for _ in range(n):
    for c in input().lower():
        symbols.add(c)
        
print(len(symbols))

