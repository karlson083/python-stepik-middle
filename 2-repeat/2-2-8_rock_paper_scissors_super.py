import os, math
clear = lambda: os.system('cls')
clear()

timur_choise, ruslan_choise = input(), input()
choise = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']

if choise.index(timur_choise) == choise.index(ruslan_choise):
    print('ничья')
elif (choise.index(timur_choise) - choise.index(ruslan_choise)) % 2 == 0:
    if choise.index(timur_choise) > choise.index(ruslan_choise):
        print('Тимур')
    else:
        print('Руслан')    
elif (choise.index(timur_choise) - choise.index(ruslan_choise)) % 2 != 0:
    if choise.index(timur_choise) < choise.index(ruslan_choise):
        print('Тимур')
    else:
        print('Руслан')    


##### v2
timur = input()
ruslan = input()
hands = ['Спок', 'ножницы', 'бумага', 'камень', 'ящерица']
winner = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(winner[hands.index(timur) - hands.index(ruslan)])


g = ('ножницы', 'бумага', 'камень', 'ящерица', 'Спок')
dist = (g.index(input()) - g.index(input())) % len(g)
print(('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])