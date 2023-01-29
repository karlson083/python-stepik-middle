import os, math
clear = lambda: os.system('cls')
clear()


timur_choise, ruslan_choise = input(), input()
winner = ''

if timur_choise != ruslan_choise:
    if timur_choise == 'камень' and ruslan_choise == 'ножницы':
        winner = 'timur'
    elif timur_choise == 'ножницы' and ruslan_choise == 'камень':
        winner = 'ruslan'
    elif timur_choise == 'ножницы' and ruslan_choise == 'бумага':
        winner = 'timur'
    elif timur_choise == 'бумага' and ruslan_choise == 'ножницы':
        winner = 'ruslan'
    elif timur_choise == 'бумага' and ruslan_choise == 'камень':
        winner = 'timur'
    elif timur_choise == 'камень' and ruslan_choise == 'бумага':
        winner = 'ruslan'

if winner == 'timur':
    print('Тимур')
elif winner == 'ruslan':
    print('Руслан')
else:
    print('ничья')


##### v2

x, y = input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])

