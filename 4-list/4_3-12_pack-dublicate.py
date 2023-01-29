import os
clear = lambda: os.system('cls')
clear()

str_input = 'a b c d'
#str_input = input()
str_input = str_input.replace(' ','')
flg = False
res_out = []
list_tmp = list(str_input[0])

for i in range(1,len(str_input)):
    if str_input[i] == list_tmp[-1]:
        list_tmp.append(str_input[i])
        flg = False
    else:
        res_out.append(list_tmp)
        list_tmp = []
        list_tmp.append(str_input[i])
        flg = True
if flg:
    res_out.append(list_tmp)
print(res_out)



#for i in str_input:
    



###### v2


str_input = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
#str_input = input()
str_input = str_input.replace(' ','')
res_out = []
res_out.append(list(str_input[0]))
count1 = 0


for i in range(1,len(str_input)):
    if str_input[i] == res_out[count1][-1]:
        res_out[count1].append(str_input[i])
    else:
        res_out.append(list(str_input[i]))
        count1 += 1

print(res_out)


###### v3

res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)

