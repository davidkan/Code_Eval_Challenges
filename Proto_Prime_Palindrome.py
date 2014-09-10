def pr(n):
    return not any(n % d == 0 for d in range(2, n // 2 + 1))


def pal(n):
    s = str(n)
    return s == s[::-1]


if __name__ == '__main__':
    for i in range(1000, 0, -1):
        if pr(i) and pal(i):
            print(i)
            exit(0)
