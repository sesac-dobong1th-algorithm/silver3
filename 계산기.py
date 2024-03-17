import sys

input = sys.stdin.readline
input()
li = input().split()
s = 2  # 2 = 최고차항 계수가 1일라서 X만 입력과 마지막 = 입력 수
for i in li[1:-1]:
    # 계수가 0이면 *, X 입력으로 +2
    if i == "0":
        s += 2
    # 계수가 있으면 +, 숫자, * X 입력으로 +(3 + 숫자 길이)
    else:
        s += len(i) + 3
# 실수항이 있으면 +, 숫자 입력 -> +(1 + 숫자 길이)/ 실수항이 0이면 끝
s += 1 + len(li[-1]) if li[-1] != "0" else 0
print(s)

# 짧게 작성한 코드
# input()
# s = 0
# for i in input().split()[1:]:
#     s += len(i) + 3
#     if i == "0": s -= 2
# print(s)
