import sys


def main():
    input = sys.stdin.readline

    # 부분 수열에 포함되는 숫자의 존재 여부(갯수)를 확일할 리스트
    nums = [0] * 11

    # s: 부분 수열의 첫 원소의 원래 인덱스
    # ans, tmp: 부분 수열의 길이(정답, 현재)
    s = ans = tmp = 0
    input()

    arr = list(map(int, input().split()))
    for a in arr:
        nums[a] += 1
        tmp += 1

        # li: 부분 수열에 존재하는 숫자만 모아둔 리스트
        li = [i for i, j in enumerate(nums) if j]

        # li는 오름차순이라서 처음과 마지막 원소가 최솟값, 최댓값임
        if li[-1] - li[0] > 2:
            nums[arr[s]] -= 1
            tmp -= 1
            s += 1

        # 가능한 부분 수열 중 길이를 최댓값 업데이트
        if ans < tmp:
            ans = tmp
    print(ans)


main()
