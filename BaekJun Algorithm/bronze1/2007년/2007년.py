if __name__ == '__main__' :
    x, y = map(int, input().split())

    day1 = [1, 3, 5, 7, 8, 10, 12]
    day2 = [4, 6, 9, 11]
    day3 = [2]
    dp = [0]

    m = 0
    for i in range(1, x) :
        if i in day1 :
            m += 31
        elif i in day2 :
            m += 30
        else :
            m += 28

    result = m + y
    ct = result % 7
    if ct == 0 :
        print("SUN")
    elif ct == 1 :
        print("MON")
    elif ct == 2 :
        print("TUE")
    elif ct == 3 :
        print("WED")
    elif ct == 4 :
        print("THU")
    elif ct == 5:
        print("FRI")
    elif ct == 6:
        print("SAT")