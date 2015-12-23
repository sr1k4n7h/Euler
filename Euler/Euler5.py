__author__ = 'sr1k4n7h'

from fractions import gcd
print '\n'.join(str(reduce(lambda a, b: (a*b)/gcd(a, b), range(1, int(input()) + 1))) for c in range(int(input())))
