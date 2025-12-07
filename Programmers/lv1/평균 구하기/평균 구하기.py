def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(solution(arr))