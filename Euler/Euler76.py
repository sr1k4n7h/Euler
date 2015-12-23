
__author__='sr1k4n7h'

partitions = {}
def partition(n):
    if n < 0: return 0
    if n == 0: return 1
    if n not in partitions:
        L = 0
        for k in range(1, n+1):
            L += (-1)**(k+1) * (partition(n - (k * (3 * k - 1) // 2)) + partition(n - (k * (3 * k + 1) // 2)))
        partitions[n] = L % 1000000007
    return partitions[n]

def main():
    for _ in range(int(raw_input())):
        print(partition(int(raw_input())) - 1)

if __name__ == "__main__": main()
