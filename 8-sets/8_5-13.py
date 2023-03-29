import os, math
clear = lambda: os.system('cls')
clear()


text_input = input().lower()

for i in '.,;:-?!':
    text_input = text_input.replace(i,'')
out_set = set(text_input.split())

print(len(out_set))




###### v2


