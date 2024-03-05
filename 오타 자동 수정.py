import sys


def sol(x):
    # 한 글자를 적게/많이 썼을 때
    def less_more(n, m, s1, s2, t=0):
        for i in range(n):
            if t == 2:
                return False
            if s1[i] == s2[i + t]:
                continue
            elif i + t + 1 < m and s1[i] == s2[i + t + 1]:
                t += 1
            else:
                return False
        return True

    # 한 글자를 잘못 적었을 때 / 인접한 두 글자의 순서가 잘못 되었을 때
    def wrong_switch(n, s1, s2, c=0):
        for i in range(n):
            if s1[i] != s2[i]:
                c += 1
                if c == 2:
                    return False
                elif i < n - 1 and s1[i] == s2[i + 1] and s1[i + 1] == s2[i]:
                    c -= 1
        return True

    # 단어 사전에 있는 단어인 경우
    if x in dict_li:
        return x + li[0]
    n = len(x)

    # 비슷한 단어가 있는 경우
    for word in dict_li:
        if (m := len(word)) == n + 1 and less_more(n, m, x, word):
            return x + li[1] + word
        if m == n - 1 and less_more(m, n, word, x):
            return x + li[1] + word
        if m == n and wrong_switch(n, x, word):
            return x + li[1] + word

    # 위 두 경우가 아닐 때
    return x + li[2]


if __name__ == "__main__":
    input = sys.stdin.readline
    li = (" is correct", " is a misspelling of ", " is unknown")
    dict_li = [input().strip() for _ in range(int(input()))]
    print("\n".join([sol(input().strip()) for _ in range(int(input()))]))
