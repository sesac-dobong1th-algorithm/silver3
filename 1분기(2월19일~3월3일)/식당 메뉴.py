import sys
from collections import deque


# 오름차순 정렬후 빈칸을 사이에 두고 이어붙인 문자열 반환, 없으면 None 반환
def sol(li: list) -> str:
    return " ".join(map(str, sorted(map(int, li)))) or "None"


def main():
    input = sys.stdin.readline
    # 본인이 좋아하는 메뉴를 먹은 학생 목록 A
    # 본인이 좋아하지 않는 메뉴를 먹은 학생 목록 B
    # 학교 식당에 도착하였으나 식사를 하지 못한 학생 목록 C
    A, B, C = [], [], deque([])

    for _ in range(int(input())):
        type_, *num = input().split()
        # 학생 정보가 들어오면 C에 저장
        if type_ == "1":
            C.append(num)
        else:
            # deque를 사용해서 맨 앞의 원소에 대한 접근을 빠르게 함
            a, b = C.popleft()
            # 준비된 음식과 기다린 학생이 좋아하는 메뉴가 같으면 A에 저장
            if num[0] == b:
                A.append(a)
            # 아니면 B에 저장
            else:
                B.append(a)
    # A, B, C에 저장된 목록을 줄바꿈하며 출력
    print("\n".join((sol(A), sol(B), sol((a for a, _ in C)))))


if __name__ == "__main__":
    main()


# deque 사용 안하고 작성한 코드
# import sys


# def sol(li):
#     return " ".join(map(str, sorted(map(int, li)))) or "None"


# def main():
#     input = sys.stdin.readline
#     A, B, C, F = [], [], [], []
#     for _ in range(int(input())):
#         type_, *num = input().split()
#         if type_ == "1":
#             C.append(num)
#         else:
#             F.append(num[0])
#     for i in range(n := len(F)):
#         (a, b), f = C[i], F[i]
#         if f == b:
#             A.append(a)
#         else:
#             B.append(a)
#     print("\n".join((sol(A), sol(B), sol((a for a, _ in C[n:])))))


# if __name__ == "__main__":
#     main()
