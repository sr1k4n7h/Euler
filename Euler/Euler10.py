__author__ = 'sr1k4n7h'

limit_n = 1000007
se = [0] * limit_n
for i in range(2, limit_n):
    if se[i]:
        continue
    for f in xrange(i * 2, limit_n, i):
        se[f] = 1
for _j in range(2, limit_n):
    se[_j] = se[_j - 1] + (0 if se[_j] else _j)
for _i in range(int(raw_input())):
    print(se[int(raw_input())])

