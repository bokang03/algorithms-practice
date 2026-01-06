import sys

if __name__ == '__main__':
    arr = []
    end = 0
    ct = 0

    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])

    arr.sort(key = lambda x : (x[1],x[0]))

    for stPoint, endPoint in arr :
        if end <=stPoint :
          ct += 1
          end = endPoint

    print(ct)