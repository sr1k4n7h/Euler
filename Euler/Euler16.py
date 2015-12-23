__author__ = 'sr1k4n7h'

A = [2**k for k in range(10001)]
for _ in range(int(input())):
    n = A[int(input())]
    print(sum([int(digit) for digit in str(n)]))