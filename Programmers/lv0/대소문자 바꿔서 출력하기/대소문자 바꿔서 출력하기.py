if __name__ == '__main__' :
    str = input()

    for i in str:
        k = ord(i)
        if k < 97:
            s = k + 32
            s = chr(s)
            print(s, end="")
        else:
            s = k - 32
            s = chr(s)
            print(s, end="")
    # print(input().swapcase())