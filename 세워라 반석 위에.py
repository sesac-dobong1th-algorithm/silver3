# import sys
# from collections import deque


# def check(num):
#     li = [i for i, j in enumerate(num) if j]
#     return li[-1] - li[0] <= 2


# def main():
#     input = sys.stdin.readline
#     input()
#     num = [0] * 11
#     q = deque([])
#     ans = 1
#     for a in map(int, input().split()):
#         q.append(a)
#         num[a] += 1
#         while not check(num):
#             num[q.popleft()] -= 1
#         if ans < (t := len(q)):
#             ans = t
#     print(ans)


# main()


import sys


def main():
    input = sys.stdin.readline
    nums = [0] * 11
    s = ans = tmp = 0
    input()
    arr = list(map(int, input().split()))
    for a in arr:
        nums[a] += 1
        tmp += 1
        li = [i for i, j in enumerate(nums) if j]
        if li[-1] - li[0] > 2:
            nums[arr[s]] -= 1
            tmp -= 1
            s += 1
        if ans < tmp:
            ans = tmp
    print(ans)


main()


# import sys
# def main():
#     input = sys.stdin.readline
#     n = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#     for s in range(n - 1):
#         M = m = arr[s]
#         for e in range(s + 1, n):
#             if M < (t := arr[e]):
#                 M = t
#             elif m > t:
#                 m = t
#             if M - m > 2:
#                 break
#             if ans < (l := e - s + 1):
#                 ans = l
#     print(ans)
# main()


# import sys
# def main():
#     input = sys.stdin.readline
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for length in range(n, 0, -1):
#         for start_idx in range(n - length + 1):
#             tmp = set(arr[start_idx : start_idx + length])
#             M, m = max(tmp), min(tmp)
#             if M - m <= 2:
#                 print(length)
#                 return
# main()
