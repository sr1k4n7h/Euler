__author__ = 'sr1k4n7h'

s = lambda n: int(n * (n + 1) / 2)
r = lambda n: int(s(int(n / 3)) * 3 + s(int(n / 5)) * 5 - s(int(n / 15)) * 15)
print '\n'.join(str(r(int(raw_input())-1)) for i in xrange(int(raw_input())))
