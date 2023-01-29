import os, math
clear = lambda: os.system('cls')
clear()

s = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
#s = input()
max_r = 0
cnt_r = 0

for i in s:
    if i == 'Р':
        cnt_r += 1
        if cnt_r > max_r:
            max_r = cnt_r
    else:
        cnt_r = 0

print(max_r)




###### v2
s = input().split('О')
print(len(max(s)))