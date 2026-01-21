from itertools import permutations


def solution(k, dungeons):
    answer = -1
    d = [i for i in range(len(dungeons))]
    p = []

    v = permutations(d, len(d))
    p.extend(v)

    max_num = 0

    for i in p:
        ct = 0
        piro = k
        for j in i:  # 0, 1, 2
            if piro < dungeons[j][0]:
                break
            else:
                piro -= dungeons[j][1]
                ct += 1
        if max_num < ct:
            max_num = ct

    return max_num


if __name__ == '__main__':
    k = 80
    dungeons = 	[[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))
