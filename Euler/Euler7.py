__author__ = 'sr1k4n7h'

primes = [2, 3, 5, 7]
next = 11
while 10000 >= len(primes):
    limit = next ** 0.5
    for p in primes:
        if p > limit:
            primes.append(next)
            break
        if next % p == 0:
            break
    next += 2
for c in range(int(input())):
    print(primes[int(input()) - 1])
