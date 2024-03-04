import sys

N, L, W, H = map(int, sys.stdin.readline().split())

# right는 min(L,W,H)나 한 변의 최대 길이 1,000,000,000으로 할 수 있음
# 1,000,000,000일 때는 확인 안해봤지만 for문을 80~100 정도 반복 해야함
left, right = 0, (L * W * H / N) ** (1 / 3)

for _ in range(40):
    mid = (left + right) / 2
    if (L // mid) * (W // mid) * (H // mid) < N:
        right = mid
    else:
        left = mid
print(f"{left:.9f}")

# 이진탐색
# 큰 박스안에 N개를 못 넣으면 right를 mid로 갱신
# N개 이상 가능하면 left를 mid로 갱신

# 소수점 이하 값도 고려해야해서 2로 나눌 때, //이 아닌 /를 사용
# 갱신시 mid +1, -1이 아니라 mid 사용
# 그래서 다른 이진 탐색처럼 while left <(=) right 사용하면 무한 루프

# 정수 값을 구하는 거였으면 2^30 > 1,000,000,000이라면 30회 정도면 될텐데,
# 소수점이라서 조금 더 반복함,,
