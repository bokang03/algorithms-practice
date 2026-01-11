import sys
import heapq as hq

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    n = int(input())
    heap = []

    for _ in range(n):
        num = int(input())

        if num > 0:
            # Python의 heapq는 최소 힙이므로,
            # 최대 힙을 구현하기 위해 음수로 바꾸어 저장합니다.
            hq.heappush(heap, -num)
        else:
            # num이 0인 경우
            if heap:
                # 가장 작은 값(음수화된 최대값)을 꺼내어 다시 양수로 바꿉니다.
                print(-hq.heappop(heap))
            else:
                # 힙이 비어있다면 0을 출력합니다.
                print(0)

if __name__ == '__main__':
    solve()