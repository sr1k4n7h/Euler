__author__ = 'sr1k4n7h'

fact = [1] * 15
for j in range(1, 15):
    fact[j] = fact[j - 1] * j


def perm(a, N):
    if not a: return ''
    n = len(a)
    i = 0
    while fact[n - 1] <= N:
        N -= fact[n - 1]
        i += 1
    #   print(i,n,a[:i], a[i+1:])
    return a[i] + perm(a[:i] + a[i + 1:], N)


for _ in range(int(input())):
    print(perm(list('abcdefghijklm'), int(input()) - 1))
