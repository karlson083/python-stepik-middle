import os, math
clear = lambda: os.system('cls')
clear()

first_string_song = 'тимур' + ' запретил букву '
#first_string_song = input() + ' запретил букву '

char_string = list(set(first_string_song.replace(' ','')))
char_string.sort()

#spis_song = first_string_song.split()

#print(first_string_song, char_string)

for i in char_string:
    print(first_string_song + i)
    first_string_song = first_string_song.replace(i, '').replace('  ',' ').lstrip()



###### v2
