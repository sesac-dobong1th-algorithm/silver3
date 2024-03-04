# 파이썬이라서 큰 수 영향 x
print(int(input()) * 2 - 2 or 1)

# 큰 수 연산 정밀도 고려 코드
N = input()
carry = 0
ans = []
i = 1
for digit in map(int, N[::-1]):
    n = (digit - i) * 2 + carry
    i = 0
    carry = n // 10
    ans.append(n % 10)
if carry:
    ans.append(carry)
print("".join(map(str, ans[::-1])))
