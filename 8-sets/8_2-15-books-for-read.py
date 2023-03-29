import os, math
clear = lambda: os.system('cls')
clear()

n, m, k, x, y, z, t, a = 19, 18, 22, 32, 33, 35, 2, 50

#n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]


nm = n + m - x - t
mk = m + k - y - t
kn = k + n - z - t
two = nm + mk + kn
one = n + m + k - (2 * two) - (3 * t)
zero = a - one - two - t

print(one, two, zero, sep = '\n')




###### v2


n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

i = n + m + k
j = x + y + z

print(3 * (t - i) + 2 * j)
print(2 * i - j - 3 * t)
print(a + i - j - t)