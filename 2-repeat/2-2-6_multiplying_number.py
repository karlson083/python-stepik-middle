import os, math
clear = lambda: os.system('cls')
clear()


numbers = [int(input()) for _ in range(int(input()))]
mult = int(input())
multiply = []
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if i != j:
            multiply.append(numbers[i] * numbers[j])
#           print(numbers[i],' * ',numbers[j], ' = ', numbers[i] * numbers[j], sep = '')
if mult in multiply:
    print('ДА')
else:
    print('НЕТ')

##### v2

