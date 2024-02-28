# 리스트 사용
import sys

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0:
        break

    # 개행문자, 띄어쓰기 제거 / 대문자로 변환
    message = "".join(input().rstrip().split()).upper()
    i, j, length = 0, 0, len(message)
    tmp = [""] * length

    # n칸 씩 띄우며 문자열 순서 재배치
    for k in range(length):
        tmp[i] = message[k]
        i += n
        if i >= length:
            i = (j := j + 1)
    ans.append("".join(tmp))
print("\n".join(ans))


# 딕셔너리 사용
import sys

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0:
        break
    message = "".join(input().rstrip().split()).upper()
    tmp, i, j, length = {}, 0, 0, len(message)
    for k in range(length):
        tmp[i] = message[k]
        i += n
        if i >= length:
            i = (j := j + 1)
    ans.append("".join(map(lambda x: x[1], sorted(tmp.items(), key=lambda x: x[0]))))
print("\n".join(ans))


# 슬라이싱 사용
import sys

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0:
        break
    message = "".join(input().rstrip().split()).upper()
    q, r = len(message) // n, len(message) % n
    s, e, tmp = 0, q - 1, []

    for i in range(n):
        if i < r:
            tmp.append(message[s : e + 2])
        else:
            tmp.append(message[s : e + 1] + " ")
        s = e + 1
        e += q

    for j in range(q + 1):
        encrypted = ""
        for i in range(n):
            encrypted += tmp[i][j]
    ans.append(encrypted.rstrip())
print("\n".join(ans))


# import sys
# input = sys.stdin.readline
# ans = []
# while True:
#     if (n := int(input())) == 0: break
#     message = "".join(input().rstrip().split()).upper()
#     q, r, e = len(message) // n, len(message) % n, -1
#     tmp = [message[e + 1 : (e := e + q + bool(i < r)) + 1] + " " * bool(i >= r) for i in range(n)]
#     ans.append("".join(("".join((tmp[i][j] for i in range(n))).rstrip() for j in range(q + 1))))
# print("\n".join(ans))
