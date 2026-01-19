from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0

    while True:
        num = queue.popleft()

        # 마지막 순서일 경우
        if len(queue) == 0:
            return answer + 1

        # 검증 숫자가 작은 경우 뒤로 보냄
        if num < max(queue):
            queue.append(num)
        # 검증 숫자가 최댓값이므로 실행으로 추가, 및 location 횟수 확인
        else:
            answer += 1
            if location == 0:
                return answer

        if location == 0:
            location = len(queue) - 1
        else:
            location -= 1

if __name__ == '__main__' :
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))