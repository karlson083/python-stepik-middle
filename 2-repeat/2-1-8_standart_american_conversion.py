import os, math
clear = lambda: os.system('cls')
clear()


x = input()
r = len(x) // 3
st = len(x) % 3
out = ''

if st > 0:
    out = x[:st]

if len(x) > 3:
    for i in range(0,r):
        out = out + ',' + x[i*3+st:i*3+st+3]
else:
    out = x

if out[0] == ',':
    out = out[1:]
print(out)


# v2
'''
num = input()
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)


s = input()
n = []

while len(s) > 0:
    n.append(s[-3:])
    s = s[:-3]
    
new_n = n[:: -1]
print(*new_n, sep = ',')
'''







