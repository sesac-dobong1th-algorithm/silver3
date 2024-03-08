# 두 가지 방법으로 풀었습니다.

import sys


# 첫번째 열을 먼저 채운 후
# (0, 0) -> (0, N) -> (1, 0) -> ... -> (N-1, N-1)
# 순서대로 채워 넣기
def main():
    input = sys.stdin.readline
    n, x = int(input()), int(input())
    n2 = n * n
    snail, m = [[n2 - i] + [0] * (n - 1) for i in range(n)], (n - 1) // 2
    r = c = m
    if x in range(n * (n - 1) + 1, n2 + 1):
        r, c = n2 - x, 0
    t = 1
    for i in range(n):
        prev = snail[i][0]
        if i == m:
            t = 0
        for j in range(1, n):
            num = 1
            if j <= i + t:
                if t or i != n - 1 and j <= m - i % m:
                    num = (n - 2 * j + 1) * 4 - 1
                num *= -1
            elif n - j <= (i * t) - (2 * m - i) * (t - 1):
                num = (2 * j - n) * 4 - 1
            prev = snail[i][j] = prev + num
            if prev == x:
                r, c = i, j
    print("\n".join(map(lambda x: " ".join(map(str, x)), snail)))
    print(r + 1, c + 1)


main()


# 달팽이 모양대로 가운데부터 가장자리로
# 1 부터 N^2 까지 차례대로 숫자 채우기
def main():
    input = sys.stdin.readline

    N = int(input())
    x = int(input())
    dxs = (0, 1, 0, -1)
    dys = (1, 0, -1, 0)

    td = [[[] for _ in range(N)] for _ in range(N)]
    M = (N - 1) // 2
    r = c = M + 1
    o = [M, M]
    td[M][M] = num = 1
    for i in range(1, N, 2):
        o[0] -= 1
        o[1] -= 1
        for dx, dy in zip(dxs, dys):
            for _ in range(i + 1):
                o[0] += dx
                o[1] += dy
                num += 1
                td[o[0]][o[1]] = num
                if num == x:
                    r, c = o[0] + 1, o[1] + 1
    print("\n".join(map(lambda x: " ".join(map(str, x)), td)))
    print(r, c)


if __name__ == "__main__":
    main()
