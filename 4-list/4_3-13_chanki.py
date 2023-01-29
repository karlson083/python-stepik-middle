import os
clear = lambda: os.system('cls')
clear()

list_in = 'a b c d e f r g b'.split()
n = 3

#list_in = input().split()
#n = int(input())


def chunked(list_out,n1):
    list_out = []
    for ch in list_in:
        if list_out and len(list_out[-1]) < n1:
            list_out[-1].append(ch)
        else:
            list_out.append([ch])
    return list_out

print(chunked(list_in,n))

###### v2


def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))