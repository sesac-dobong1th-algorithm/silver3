import sys


# 시간:분 -> 분으로 단위 변경하는 함수
def hhmm2min(t: str) -> int:
    t = list(map(int, t.split(":")))
    return t[0] % 12 * 60 + t[1]


# 세 시각의 차이를 구하는 함수
# t1 < t2 < t3라는 가정 하에서 t2과 t1, t3와 t2 사이의 시간을 구해서 비교합니다.
def compare(t1, t2, t3):
    if (diff := (t2 - t1) % 720) == (t3 - t2) % 720:
        return diff
    return 0


input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    # 시간을 입력 받아서 분으로 저장
    t1, t2, t3 = map(hhmm2min, input().rstrip().split())

    # 모든 가능 한 경우에 대해서
    for a, b, c in (
        (t1, t2, t3),
        (t1, t3, t2),
        (t2, t1, t3),
        (t2, t3, t1),
        (t3, t1, t2),
        (t3, t2, t1),
    ):

        # 시차가 같은 경우가 존재하면
        if diff := compare(a, b, c):
            # 시차가 4시간이면, 어떤 시계가 맞는지 확인 할 수 없음
            if diff == 240:
                ans.append("Look at the sun")
            # 그 외에 시차가 480분 이하면, 가운데 시각을 가르키는 시계가 맞음
            elif diff < 480:
                ans.append(
                    f"The correct time is {b // 60 or 12}:{str(b % 60).zfill(2)}"
                )
            # 480 분 초과는 무시
            else:
                continue
            break

print("\n".join(ans))
