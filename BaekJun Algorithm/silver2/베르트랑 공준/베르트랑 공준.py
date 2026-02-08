import sys

def validate(num):
    result = True
    for i in range(2, int(num**0.5)+1):
        if num%i == 0 :
            result = False
            break
    if result :
        return  1
    else : return 0

if __name__ == "__main__":
    input = sys.stdin.readline
    ans = []
    dp = [-1] * ((123456 * 2) + 1)
    dp[1] = 0

    while True :
        n = int(input())
        if n == 0 :
            break
        elif n == 1 :
            print(1)
        else :
            ct = 0
            for num in range(n+1, 2 * n + 1):
                if dp[num] == -1 :
                   dp[num] = validate(num)
                   ct += dp[num]
                else :
                    ct += dp[num]
            print(ct)