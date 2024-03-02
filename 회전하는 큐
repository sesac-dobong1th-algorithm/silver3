N, M = map(int, input().split())
q = list(range(1, N + 1))
# ans: 좌우로 움직인 횟수, t: 이전 움직임에 따라서 반영할 인덱스
ans = t = 0

for a in map(int, input().split()):
    # a: 초기 상태의 뽑아낼 위치
    # x: 현재 상태의 뽑아낼 위치(q를 좌우로 안 옮김)
    # k: 현재 상태의 뽑아낼 위치(q를 좌우로 옮겼다면,,)
    x = q.index(a)
    k = x - t
    q.pop(x)
    
    # y: 좌우로 움직여야 하는 최소 칸 수
    y = k % N
    if y > (k := -k % N): y = k
    N -= 1
    ans += y
    t = x

print(ans)
