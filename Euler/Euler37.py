__author__ = 'sr1k4n7h'

A = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
N = int(input())
print(sum(filter(lambda x: x <= N, A)))
