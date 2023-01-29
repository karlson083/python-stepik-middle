import os, math
clear = lambda: os.system('cls')
clear()


s_input = input().split()
s_output = []
for i in range(len(s_input)):
    s_output.append(int(s_input[i - 1]))
print(*s_output)


##### v2
a = input().split()

print(*[a[-1]] + a[:-1])

