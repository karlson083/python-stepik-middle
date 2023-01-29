import os, math
clear = lambda: os.system('cls')
clear()


s_input = input().split()
s_unical = []
for i in s_input:
    if i not in s_unical:
        s_unical.append(i)
print(len(s_unical))


##### v2

