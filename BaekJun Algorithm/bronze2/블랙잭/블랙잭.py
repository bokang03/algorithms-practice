from itertools import permutations

if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    total = []

    number = permutations(cards, 3)
    total.extend(number)

    ct = -1

    for i in total :
        i = sum(list(i))
        if m >= i :
            if m - i < m - ct :
                ct = i

    print(ct)