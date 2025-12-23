import sys

if __name__ == '__main__':
    result = []
    for _ in range(int(sys.stdin.readline())):
        n = input()
        if n.count("(") != n.count(")") : # 개수가 맞지 않을 때
            result.append("NO")
            continue

        if n[-1] == "(" :
            result.append("NO")
            continue

