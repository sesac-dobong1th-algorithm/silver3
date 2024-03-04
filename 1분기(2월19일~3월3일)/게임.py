# 분수부등식 풀이
import sys

X, Y = map(int, sys.stdin.readline().split())
if (Z := (Y * 100) // X) >= 99:
    print(-1)
else:
    if int(i := (X * (Z + 1) - 100 * Y) / (99 - Z)) == i:
        print(i)
    else:
        print(i + 1)


# 분수부등식을 짧게 작성
# X,Y=map(int,input().split())
# print(bool((Z:=(Y*100)//X)>=99)*-1 or bool(int(i:=(X*(Z+1)-100*Y)/(99-Z))!=i)+int(i))


# 이진 탐색 코드
import sys

X, Y = map(int, sys.stdin.readline().split())
Z = (Y * 100) // X


# 승률이 Z보다 큰지 확인하는 함수
def check(n):
    if (Y + n) * 100 // (X + n) > Z:
        return True
    else:
        return False


# 이진 탐색
def bin_search():
    left, right = 1, 1_000_000_000  # 탐색할 최솟값, 최댓값
    while left <= right:
        m = (left + right) // 2
        # 평균이 승률을 올리면 최댓값을 내임
        if check(m):
            right = m - 1
        # 아니면 최솟값을 올림
        else:
            left = m + 1
    return left  # 최솟값 반환


if Z >= 99:  # 승률 99나 100은 올릴 수 없음
    print(-1)
else:
    print(bin_search())
