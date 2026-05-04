if __name__ == '__main__':
    def calc(a, b, c):
        if b == 1:
            return a % c
        else:
            k = calc(a, b // 2, c)
            if b % 2 == 0:
                return (k * k) % c
            else:
                return (k * k * a) % c


    a, b, c = map(int, input().split())
    print(calc(a, b, c))