import sys


# 놀라운(surprising) 문자열인지 아닌지 확인 후 ans에 저장하는 함수
def sol():
    if (n := len(string)) < 3:  # 철자 수가 2개 이하는 놀라운 문자열임
        ans.append(string + surprising)
    else:
        for i in range(n - 1):
            tmp = set()
            for j in range(n - i - 1):
                # 집합을 통해서 D쌍의 유일성 확인
                if (k := string[j] + string[j + i + 1]) in tmp:
                    ans.append(string + not_surprising)
                    return
                else:
                    tmp.add(k)
        ans.append(string + surprising)


# 초기 세팅
input, ans = sys.stdin.readline, []
surprising, not_surprising = " is surprising.", " is NOT surprising."

# '*'이 입력되기 전까지 계속 실행
while (string := input().strip()) != "*":
    sol()
print("\n".join(ans))  # 정답을 줄바꿈하며 출력
