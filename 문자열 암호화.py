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


# 틀린 코드
import sys
from math import ceil

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0:
        break
    message = "".join(input().rstrip().split()).upper()
    q = ceil(len(message) / n)
    ans.append("".join((message[i::q] for i in range(q))))
print("\n".join(ans))
