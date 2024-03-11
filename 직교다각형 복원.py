def main():
    a = open(0)
    _, ans = next(a), 0

    # 가로, 세로를 각각 기록함
    rows = [[] for _ in range(10001)]
    cols = [[] for _ in range(10001)]
    for p in a:
        i, j = map(int, p.split())
        rows[i].append(j)
        cols[j].append(i)

    # 행, 열별로 정렬한 후 두 점씩 거리 계산 후 합산
    for row in rows:
        row.sort()
        for i in range(0, len(row), 2):
            ans += row[i + 1] - row[i]
    for col in cols:
        col.sort()
        for i in range(0, len(col), 2):
            ans += col[i + 1] - col[i]
    print(ans)


main()
