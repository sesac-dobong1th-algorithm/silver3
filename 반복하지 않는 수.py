# itertools를 활용헤서 모든 경우를 직접 확인하기보다
# iterator로 원하는 값에만 접근해서 사용 메모리를 줄인 코드

# from itertools import permutations, chain, islice
# from math import perm

# ans = []
# while True:
#     n = int(input())
#     if n == 0: break
#     ans.append("".join(map(str, next(islice(chain(*map(lambda x: islice(permutations(range(10), x), perm(9, x - 1), None),range(1, 11))), n - 1, None)))))
# print("\n".join(ans))


def sol(length: int, num: int, flag: bool, digits: list) -> None:
    global idx  # 겹치지 않는 숫자를 발견할 때마다 순서에 1을 더해야 하므로 global 변수 선언

    # 1,000,000번째 숫자까지만 생성
    if idx > M:
        return

    # 각 자리수에 겹치지 않는 숫자를 생성했다면 nums에 저장, idx 업데이트
    if not length:
        nums[idx] = num
        idx += 1
        return

    for digit in digits:  # 다음 자리수에 올 수 있는 숫자들 중에서
        # 첫번째 자리에 0이 오는 경우는 무시
        if flag and digit == 0:
            continue
        tmp = [i for i in digits]
        tmp.remove(digit)

        # 다음 자리수에 겹치지 않는 숫자를 두고 그 다음 자리수에 대한 탐색을 재귀적으로 이어감
        sol(length - 1, num + digit * (10 ** (length - 1)), False, tmp)


def main():
    ans = []  # 정답을 모아 둘 리스트
    for length in range(1, 9):  # 1~8 자리수 숫자를 for문으로 생성
        sol(length, 0, True, list(range(10)))

    while True:  # 계속 입력을 받다가 입력이 0인 경우 종료
        if (i := int(input())) == 0:
            break
        ans.append(nums[i])
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    import sys

    input = lambda: int(sys.stdin.readline())  # 입력 값을 숫자로 변환
    M, idx = 1_000_000, 1
    nums = [0] * (M + 1)  # n번째 숫자를 저장할 리스트 초기화
    main()


# 시간 초과

# import sys
# input = sys.stdin.readline  # 입력 값을 숫자로 변환
# ans = []  # 정답을 모아 둘 리스트

# while True:  # 계속 입력을 받음
#     if (idx := int(input())) == 0:  # 입력이 0인 경우 종료
#         break
#     n = 1
#     for _ in range(1, idx + 1):
#         num = str(n)
#         while len(set(num)) != len(num):
#             n += 1
#             num = str(n)
#         n += 1
#     ans.append(num)

# # 답을 한 줄씩 출력
# print("\n".join(ans))
