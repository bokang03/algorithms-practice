import sys

if __name__ == '__main__':
    member = {}
    for i in range(int(sys.stdin.readline())) :
        member[i] = list(input().split())

    result = dict(sorted(member.items(), key=lambda x: (int(x[1][0]), x[0])))

    for i in result :
        print(result[i][0], result[i][1])