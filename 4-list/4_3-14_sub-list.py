import os
clear = lambda: os.system('cls')
clear()

list_in = 'a b v'.split()

#list_in = input().split()


def sub_lists(list1):
    result = [[]]
    for i in range(0, len(list1)):
        for x in range(0, len(list1) - i ):
            result.append(x : i + x + 1])
    return result

print(sub_lists(list_in))


###### v2


