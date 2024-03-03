import sys

P = [[0] * 8 for _ in range(8)]  # P[i][j] = i가 j를 이길 확률
prev = i = 0
for k, p in enumerate(map(int, sys.stdin.readline().split()), 1):
    j = k - prev
    P[i][j], P[j][i] = p / 100, 1 - p / 100
    if j == 7:
        i += 1
        prev = k - i

# 1라운드 대전 상대를 이기고, 2라운드 상대가 될 수 있는 두 사람을 이길 확률을 곱함
# 2라운드 상대가 될 수 있는 두 사람과 만날 확률을 그 사람이 1라운드에서 이길 확률임
tmp = []  # 2라운드 이길 확률 저장 리스트
for n in range(1, 9):
    # a, b : 2라운드 상대 번호
    if n % 2:
        a, b = (n + 1) % 4 + (n // 4) * 4, (n + 2) % 4 + (n // 4) * 4
        tmp.append(P[n - 1][n] * (P[n - 1][a] * P[a][b] + P[n - 1][b] * P[b][a]))
    else:
        a, b = (n) % 4 + ((n - 1) // 4) * 4, (n + 1) % 4 + ((n - 1) // 4) * 4
        tmp.append(P[n - 1][n - 2] * (P[n - 1][a] * P[a][b] + P[n - 1][b] * P[b][a]))

ans = []  # 3라운드 이길 확률 저장 리스트
# 위와 비슷한 방식으로,,
for n in range(1, 9):
    if (n + 3) % 8 // 4:
        ans.append(tmp[n - 1] * sum(P[n - 1][i] * tmp[i] for i in range(4, 8)))
    else:
        ans.append(tmp[n - 1] * sum(P[n - 1][i] * tmp[i] for i in range(4)))
print(" ".join(map(lambda x: f"{x:.13f}", ans)))


# # P: 2차원에서 1차원 리스트로 작성한 코드
# import sys
# P=[0]*64
# prev=i=0
# for k,p in enumerate(map(int, sys.stdin.readline().split()),1):
#     j=k-prev
#     P[i*8+j],P[j*8+i]=p/100,1-p/100
#     if j==7:
#         i+=1
#         prev=k-i
# tmp=[]
# for n in range(1,9):
#     if n%2:
#         a,b=(n+1)%4+(n//4)*4,(n+2)%4+(n//4)*4
#         tmp.append(P[(n-1)*8+n]*(P[(n-1)*8+a]*P[a*8+b]+P[(n-1)*8+b]*P[b*8+a]))
#     else:
#         a,b=n%4+((n-1)//4)*4,(n+1)%4+((n-1)//4)*4
#         tmp.append(P[(n-1)*8+(n-2)]*(P[(n-1)*8+a]*P[a*8+b]+P[(n-1)*8+b]*P[b*8+a]))
# ans=[]
# for n in range(1,9):
#     if (n+3)%8//4:ans.append(tmp[n-1]*sum(P[(n-1)*8+i]*tmp[i] for i in range(4,8)))
#     else:ans.append(tmp[n-1]*sum(P[(n-1)*8+i]*tmp[i] for i in range(4)))
# print(" ".join(map(lambda x:f"{x:.13f}",ans)))
