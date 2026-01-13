import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    cards = list(map(int, input().split()))

    m = int(input())
    valCard = list(map(int, input().split()))


    d = {}

    for i in range(n) :
        d[cards[i]] = 0

    for i in valCard :
        if i not in d :
            print(0, end =' ')
        else : print(1, end = ' ')