import sys

# 초기 세팅

# 1번 풍선은 이미 터뜨린 상태로 시작

input = sys.stdin.readline
n = int(input())
balloon = list(range(2, n+1))
note = list(map(int, input().split()))
ans = [1]
index = 0

# 아래 과정을 반복해서 터뜨릴 풍선을 기록합니다.

# 풍선을 터뜨리면 이전 인덱스 값이 오른쪽 풍선을 의미하므로
# 이동을 오른쪽으로 하면 1만큼 덜 이동해야합니다.
# 남은 풍선 수로 modulo 연산을 해서 다음 터뜨릴 풍선의 index를 구합니다.

for i in range(1, n):
    t = note[ans[-1]-1]
    if t > 0:
        t -= 1
    index = (index + t) % (n-i)
    ans.append(balloon.pop(index))
ans += balloon
print(" ".join(map(str, ans)))
