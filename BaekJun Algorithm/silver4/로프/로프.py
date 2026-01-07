import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    ropes = []

    for _ in range(int(input())):
        rope = int(input())
        ropes.append(rope)

    ropes.sort(reverse = True)

    max_num = ropes[0]

    for i in range(1, len(ropes)):
        max_num = max(max_num ,ropes[i]* (i+1))

    print(max_num)