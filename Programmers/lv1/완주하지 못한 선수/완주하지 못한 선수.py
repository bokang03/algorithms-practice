def solution(participant, completion):
    set_participant = set(participant)
    set_completion = set(completion)
    result = list(set_participant - set_completion)

    if len(result) != 0:
        return result[0]
    else:
        for i in completion:
            if completion.count(i) != participant.count(i):
                return i

if __name__ == '__main__' :
    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
    print(solution(participant, completion))