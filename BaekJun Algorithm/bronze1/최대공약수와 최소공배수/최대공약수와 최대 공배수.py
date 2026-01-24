import math

if __name__ == "__main__":
    n1, n2 = map(int, input().split())

    min_n = math.gcd(n1, n2)
    max_n = (n1 * n2)// min_n

    print(min_n)
    print(max_n)
