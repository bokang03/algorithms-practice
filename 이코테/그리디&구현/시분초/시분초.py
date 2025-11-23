if __name__ == '__main__' :
    N = int(input())
    ct = 0

    for t in range(N+1) :
        for m in range(60) :
            for s in range(60) :
                if '3' in str(t) + str(m) +  str(s) :
                    ct += 1

    print(ct)