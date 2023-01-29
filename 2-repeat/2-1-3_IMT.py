import os, math
clear = lambda: os.system('cls')
clear()

massa, tall = float(input()), float(input())
imt = massa / tall ** 2

if imt > 25:
    print('Избыточная масса')
elif 18.5 <= imt <= 25:
    print('Оптимальная масса')
else:
    print('Недостаточная масса')