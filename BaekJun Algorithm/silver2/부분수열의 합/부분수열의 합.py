import sys
from itertools import combinations

if __name__ == "__main__":
    input = sys.stdin.readline

    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    k = []

    for i in range(1, n+1):
        k.extend(map(sum, combinations(arr,i)))

    print(k.count(s))


