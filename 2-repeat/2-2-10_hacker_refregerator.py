import os, math
clear = lambda: os.system('cls')
clear()

hack_refregerators = ['222anton456','a1n1t1o1n1','0000a0000n00t00000o000000n','gylfole','richard','ant0n','antoooooooooooooooooooooooooooooooooooooooooooooooooooon']


#hack_refregerators = [input() for _ in range(int(input()))]


name_hacker = 'anton'
check_name_hacker = ''

number_refregerators_bad = []

for i in hack_refregerators:
    check_name_hacker = ''
    for j in i:
        if j == name_hacker[len(check_name_hacker)]:
            check_name_hacker = check_name_hacker + name_hacker[len(check_name_hacker)]
        if check_name_hacker == name_hacker:
            break
    if check_name_hacker == name_hacker:
        number_refregerators_bad.append(hack_refregerators.index(i)+1)

print(*number_refregerators_bad)


###### v2

for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break  
