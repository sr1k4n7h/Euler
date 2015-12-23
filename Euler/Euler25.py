__author__ = 'sr1k4n7h'

a, b = 1, 2
A = []

while b <= 1000:
    a, b = b, a + b
    A.append(a)
