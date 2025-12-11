def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)

if __name__ == '__main__' :
    n = int(input())
    lost = list(map(int, input().split()))
    reserve = list(map(int, input().split()))
    print(solution(n, lost, reserve))