__author__ = 'sr1k4n7h'

import math

def div_gen(n):
    div_list = []
    for _i in xrange(1, int(math.sqrt(n) + 1)):
        if n % _i is 0:
            yield _i
            if _i is not n / _i:
                div_list.insert(0, n / _i)
    for div in div_list:
        yield div


A = {}
for i in range(200001):
    x = list(div_gen(i))
    A.__setitem__(i, sum(x[:-1]))

for j in range(int(input())):
    c = 0
    for k in range(int(input())):
        z = A.__getitem__(k)
        if z is not k and A.__getitem__(z) == k:
            c += k
    print(c)
