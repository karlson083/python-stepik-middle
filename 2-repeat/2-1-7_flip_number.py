import os, math
clear = lambda: os.system('cls')
clear()

x = input()
if len(x) == 5:
    y = x[-1]+x[-2]+x[-3]+x[-4]+x[-5]
elif len(x) == 6:
    y = x[-6]+x[-1]+x[-2]+x[-3]+x[-4]+x[-5]
print(int(y))


# v2

s = input()
print(int(s[:-5] + s[-5:][::-1]))