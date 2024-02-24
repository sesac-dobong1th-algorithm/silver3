import sys

input = sys.stdin.readline

# 두 원의 중심과 반지름이 주어질 때 교점의 개수를 물어보는 문제랑 같음
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 원의 중심이 같은 경우
    if x1 == x2 and y1 == y2:
        # 원이 점인 경우 -> 교점 1개
        if r1 == 0 and r2 == 0:
            print(1)
        # 반지름이 다른 경우 -> 교점 x
        elif r1 != r2:
            print(0)
        # 반지름이 같은 양수일 때 -> 원이 겹침 -> 교점 무수히 많음
        else:
            print(-1)

    # 중심이 다른 경우
    else:
        # d: 두 중심 사이의 거리
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        # r, ar: 두 반지름 길이의 합과 차
        r = r1 + r2
        ar = abs(r1 - r2)

        # 두 원이 떨어져 있거나 한 원이 다른 원을 감싼 경우
        if d > r or d < ar:
            print(0)
        # 두 교점이 생기는 경우
        elif d < r and d != ar:
            print(2)
        # 한 점에서만 만나는 경우
        else:
            print(1)
