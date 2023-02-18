import os, math
clear = lambda: os.system('cls')
clear()

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [element for element in tuples if len(element)]

print(non_empty_tuples)

###### v2
