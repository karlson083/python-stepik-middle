import os, math
clear = lambda: os.system('cls')
clear()


#1
str0 = input()

while str0.count('  ') > 0:
   str0 =  str0.replace('  ', ' ')
print(str0.count(' ') + 1)

#2
print(len(input().split()))