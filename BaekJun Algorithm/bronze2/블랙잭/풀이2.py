
if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    cards.sort()
    answer = 0

    for i in range(n) :
        a = cards[i]
        l = i+1
        r = n - 1
        while l < r :
            total = a + cards[l] + cards[r]

            if total <= m :
                if answer < total :
                    answer = total
                l += 1

            else :
                r -= 1

    print(answer)