# 버리는 나무 길이를 최소화 하는 설정 높이를 구하는 문제
# 여러가지 답이 가능하면 그 중 하나만 출력해되 됨
import sys

input = sys.stdin.readline
input()  # 설정 목록 수 <- 굳이 필요 없음
hs = map(int, input().split())  # 설정 높이 목록
t = int(input())  # 나무 높이
best_setting, waste = 0, t  # 가장 좋은 높이, 버려지는 양 초기값

# 모든 목록에 대해서 버려지는 양이 최솟값이 되도록 업데이트
# 가장 좋은 세팅 값도 함께 업데이트
for h in hs:
    if waste > (w := t % h):
        waste, best_setting = w, h
print(best_setting)
