def solution(n, a, b):
    ct = 1
    while True:
        if (a + 1) // 2 == (b + 1) // 2:
            return ct
        a = (a + 1) // 2
        b = (b + 1) // 2
        ct += 1