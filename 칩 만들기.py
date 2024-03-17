N, K = map(int, input().split())

# 칩의 중요도와 순번을 같이 정렬
arr = sorted(zip(map(int, input().split()), range(N)))

connected_chips = ["0"] * N
powers = ["0"] * K
# K개의 전원(N < K일 때는 N개의 전원)을 연결하는데,
# 매번 큰 수 하나에 연결하는 경우가 제일 좋은 경우임
for i, (_, j) in enumerate(arr[::-1][:K]):
    powers[i] = j + 1
    connected_chips[j] = j + 1
print("\n".join(map(str, powers + connected_chips)))
