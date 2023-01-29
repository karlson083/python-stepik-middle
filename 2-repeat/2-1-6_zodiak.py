import os, math
clear = lambda: os.system('cls')
clear()

yars_for_lookong = int(input())
zodiak_list = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(zodiak_list[yars_for_lookong % 12])