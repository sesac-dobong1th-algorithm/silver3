import sys

rt, rj, st, sj = map(float, sys.stdin.readline().split())
# (R-1) / S
# 위 식의 값을 비교하는 문제인데, 오차를 줄이기 위해서 부등식에서 양변에 sj*st를 곱해서 계산함
# 같은 이유로 st, sj에 100이 아니라 1000을 곱하고 int로 바꿈
t, j = (rt - 1) * int(sj * 1000), (rj - 1) * int(st * 1000)
if t < j:
    print("TAOYUAN")
elif t > j:
    print("JAKARTA")
else:
    print("SAME")
