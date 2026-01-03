
if __name__ == '__main__':
    n, m = map(int, input().split())

    case1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
    case2 = ['BWBWBWBW', 'WBWBWBWB'] * 4
    count = 2501

    chess = []
    for _ in range(n):
        a = input()
        chess.append(a)

    for i in range(m - 8 + 1):
        for k in range(n - 8 + 1):
            # 세로 커팅
            ct1 = ct2 = 0
            cut = chess[k: k + 8]
            # 8*8꼴
            for j in range(8):
                cut1 = cut[j][i: i + 8]
                case11 = case1[j][0: 8]
                case22 = case2[j][0: 8]
                for h in range(8):
                    if cut1[h] != case11[h]:
                        ct1 += 1
                    if cut1[h] != case22[h]:
                        ct2 += 1
            count = min(count, ct1, ct2)

    print(count)