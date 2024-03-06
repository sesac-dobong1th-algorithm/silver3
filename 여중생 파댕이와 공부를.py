import sys


def main():
    # 입력
    p = [list(input().rstrip()) for _ in range(3 * N)]
    for idx in range(N * M):
        # for i in range(1, 3*N, 3):
        #     for j in range(0, 8*M, 8):
        i, j = 1 + 3 * (idx // M), 8 * (idx % M)

        # 본문은 길이 5 또는 6의 문자열 -> k: 본문이 끝나고 시작하는 첫 '.'의 인덱스
        k = 6 + int(p[i][j + 6] != ".")

        # a + b = c 인지 아닌지에 따라서 문제 설명대로 문자 변경
        if int(p[i][j + 1]) + int(p[i][j + 3]) == int("".join(p[i][j + 5 : j + k])):
            p[i - 1][j + 1 : j + k] = p[i + 1][j + 1 : j + k] = "*" * (k - 1)
            p[i][j] = p[i][j + k] = "*"
        else:
            p[i - 1][j + 3] = p[i][j + 2] = p[i + 1][j + 1] = "/"

    # 정답 출력
    print("\n".join(map(lambda x: "".join(x), p)))


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    sys.exit(main())
