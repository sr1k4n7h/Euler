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

A = []
xx = 0
yy = 0
for i in range(1000):
    x = list(div_gen(i))
    y = sum(x[:-1])
    if y > i:
        A.append(i)
B = []
for qq in A:
    for mm in A:
        B.append(qq+mm)

for j in range(int(raw_input())):
    x = int(raw_input())
    if x in B:
        print("YES")
    else:
        print("NO")