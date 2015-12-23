__author__ = 'sr1k4n7h'

for i in range(int(raw_input())):
    s = str(raw_input())
    p, n, k, r = [], int(s.split(" ")[0]), int(s.split(" ")[1]), 0
    q, num = k, str(raw_input())
    while q <= n:
        p.append(reduce(lambda x, y: x * y, map(int, num[r:q])))
        r, q = r + 1, q + 1
    print(max(p))
