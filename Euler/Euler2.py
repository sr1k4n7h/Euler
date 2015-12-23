__author__ = 'sr1k4n7h'

for i in range(int(input())):
    x = int(input())
    a, b, s = 1, 2, 0
    while b <= x:
        if b % 2 == 0: s += b
        a, b = b, a + b
    print(s)
