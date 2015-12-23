__author__ = 'sr1k4n7h'

fact = [1] * 10
for i in range(1, 10):
    fact[i] = fact[i - 1] * i
A = []
for K in range(10, 100000):
    S = 0
    for l in str(K):
        S += fact[int(l)]
    if S % K == 0:
        A.append(K)
N = int(input())
print(sum(filter(lambda x: x <= N, A)))
