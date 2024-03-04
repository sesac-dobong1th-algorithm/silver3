from sys import stdin


# 절반을 초과해야 지배하므로 다른 군대의 병사 수를 합친 것보다 많아야 함
# 가장 많은 숫자가 절반 보다 많으면 그 숫자가 major가 될 거고,
# 절반 보다 적으면 다른 숫자가 major가 될 수 있고, 어떤 숫자가 되든 상관 없음
def find_major(li: tuple) -> str:
    major, count = "", 0
    for n in li:
        if count == 0:
            major, count = n, 1
        elif major == n:
            count += 1
        else:
            count -= 1
    return major


def main() -> None:
    for _ in range(int(input())):
        # t: 현재 땅에 있는 병사 수. li: 각각 병사의 군대 번호가 담긴 리스트
        t, *li = input().rstrip().split()

        # 절반 초과시 지배 / 아니면 전쟁 중
        if li.count(major := find_major(tuple(li))) > int(t) // 2:
            ans.append(major)
        else:
            ans.append(ing)
    print("\n".join(ans))


if __name__ == "__main__":
    input = stdin.readline
    ans, ing = [], "SYJKGW"
    main()


# # collections.Counter로 풀기
# from sys import stdin
# from collections import Counter

# input = stdin.readline
# ans = []
# ing = "SYJKGW"
# for _ in range(int(input())):
#     # t: 현재 땅에 있는 병사 수. li: 각각 병사의 군대 번호가 담긴 리스트
#     t, *li = input().rstrip().split()

#     # num: li 내 가장 많은 병사의 군대 번호, count: 그 수
#     num, count = Counter(li).most_common(n=1)[0]

#     # 절반 초과시 지배 / 아니면 전쟁 중
#     if count > int(t) / 2:
#         ans.append(num)
#     else:
#         ans.append(ing)
# print("\n".join(ans))


# # 딕셔너리로 풀기
# from sys import stdin

# input = stdin.readline
# ans = []
# ing = "SYJKGW"
# for _ in range(int(input())):
#     # t: 현재 땅에 있는 병사 수. li: 각각 병사의 군대 번호가 담긴 리스트
#     # tmp: 병사 번호의 수를 기록할 딕셔너리
#     # num: li 내 가장 많은 병사의 군대 번호, max_count: 그 수
#     t, *li = input().rstrip().split()
#     tmp, num, max_count = {}, 0, 0

#     # 병사 수 세기
#     for n in li:
#         tmp[n] = (count := tmp.get(n, 0) + 1)

#     # max_count 구하기
#     for n, count in tmp.items():
#         if max_count < count:
#             max_count, num = count, n

#     # 절반 초과시 지배 / 아니면 전쟁 중
#     if max_count > int(t) / 2:
#         ans.append(num)
#     else:
#         ans.append(ing)
# print("\n".join(ans))
