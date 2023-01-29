import os, math
clear = lambda: os.system('cls')
clear()

str0 = input()
cost = len(str0) * 60
print(cost // 100,'р.', cost % 100, 'коп.')