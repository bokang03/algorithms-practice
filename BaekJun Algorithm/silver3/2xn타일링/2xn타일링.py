def fibo(n):
    if n < 2 :
        return 1
    num = 2
    while num <= n:
        d[num] = d[num - 1] + d[num - 2]
        num += 1
    return d[n]%10007

if __name__ == "__main__":
    n = int(input())
    d = [0] * 1001
    d[0] = 1
    d[1] = 1
    print(fibo(n))