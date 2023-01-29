import os, math
clear = lambda: os.system('cls')
clear()

n = int(input()) # количество координатных точек
s = [] # список координатных точек
ch = [0,0,0,0,0] # счетчик четвертей


def check_ch(st):
    for z in range(len(st)):
        st[z] = int(st[z])
    if st[0] > 0 and st[1] > 0:
        return 1
    elif st[0] < 0 and st[1] > 0:
        return 2
    elif st[0] < 0 and st[1] < 0:
        return 3
    elif st[0] > 0 and st[1] <0:
        return 4
    else:
        return 0

for i in range(1,n+1): # проверка координатных точек
    ch[check_ch(input().split())] += 1

print('Первая четверть: ', ch[1])
print('Вторая четверть: ', ch[2])
print('Третья четверть: ', ch[3])
print('Четвертая четверть: ', ch[4])