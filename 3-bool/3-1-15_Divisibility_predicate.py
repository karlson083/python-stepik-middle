import os, math
clear = lambda: os.system('cls')
clear()

# объявление функции
def func(num1, num2):
    
    return not (num1 % num2)
    pass

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')
###### v2
