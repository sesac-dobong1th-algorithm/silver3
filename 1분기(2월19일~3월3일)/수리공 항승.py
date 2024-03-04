import sys

input = sys.stdin.readline
N, L = map(int, input().split())

# cnt: 테이프 수, e: 테이프가 막는 마지막 지점
cnt = e = 0

# 정렬해서 새는 지점을 순서대로 확인
for i in sorted(map(int, input().split())):
    # 앞서 붙이 테이프가 이미 새는 곳을 막고 있으면 지나감
    if i <= e:
        continue
    # 새로운 테이프를 붙이면 카운트 하고, 그 테이프가 감싸는 끝 지점을 기록함
    cnt += 1
    e = i + L - 1
print(cnt)
