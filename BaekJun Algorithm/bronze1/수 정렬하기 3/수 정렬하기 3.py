import sys
if __name__ == '__main__':
    d = [0] * 10001
    for _ in range(int(sys.stdin.readline())) :
        n = int(sys.stdin.readline())
        d[n] += 1

    for i in range(1, 10001) :
        if d[i] != 0 :
            for k in range(d[i]) :
                print(i)