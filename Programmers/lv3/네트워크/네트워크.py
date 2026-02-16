from collections import deque

def solution(n, computers):
    answer = 0 # 필요한 네트워크 갯수
    visited = [False] * n # 연결 확인 기록

    for i in range(n):
        if visited[i] == False: # 연결되지 않아있는 경우 실행
            visited[i] = True # 연결
            queue = deque([i])
            while queue:
                j = queue.popleft()
                for k in range(n):
                    # 아직 연결이 안되어 있으며 1이여야 함.
                    if visited[k] == False and computers[j][k] == 1 :
                        queue.append(k)
                        visited[k] = True # 연결
                    else:
                        continue
            answer += 1
        else: # 이미 연결되어 있다면 패스
            continue

    return answer

if __name__== '__main__':

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))