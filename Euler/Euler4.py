__author__ = 'sr1k4n7h'

def pal(n):
    return str(n) == str(n)[::-1]

pals = []

for l in range(100, 1000):
    for m in range(100, l + 1):
        m *= l
        if pal(m):
            pals.append(m)
pals.sort()
for i in range(int(input())):
    N, ans = int(input()), 0
    for j in pals:
        if j < N:
            ans = max(ans, j)
    print(ans)
