
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.reverse()
        money = 0
        max_num = 0
        for i in arr :
            if max_num < i :
                max_num = i
            else :
                money += max_num - i

        print(money)
