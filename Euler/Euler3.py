__author__ = 'sr1k4n7h'

for i in range(int(input())):
    N = int(input())
    z, x = 1, 1
    while x * x <= N:
        while N % x == 0:
            z = x
            N /= x
        x += 1
    if N > 1: z = N
    print(z)
