__author__ = 'sr1k4n7h'

def g(n):
    A = {}
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            A.__setitem__(i ** j, 1)
    return len(A.keys())

print(g(int(input())))
