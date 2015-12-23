__author__ = 'sr1k4n7h'

for i in range(int(raw_input())):
    N = 1000
    result = -1
    for c in range(1, N / 2):
        for b in range((N - c) / 2, (N - c)):
            if b > c: break
            a = N - b - c
            if a > b: continue
            if a*a + b*b > c*c: break
            if a*a + b*b == c*c:
                print result
                break
    print(result)

 