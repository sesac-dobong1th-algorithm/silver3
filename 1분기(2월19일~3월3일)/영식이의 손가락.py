import sys
input = sys.stdin.readline
# a: (다친 손가락을 두번 사용하는 경우 합, 한번 사용하는 경우)을 손가락 순번대로 저장한 튜플
a = ((16,8),(8,6),(8,4),(8,2),(16,8))
n = int(input())
m = int(input())
n -= 1 # 숫자를 처음 셀 때, 다친 손가락을 사용하기 전까지 셀 수 있는 수, a의 인덱스 값
print(n + a[n][0]*(m//2) + a[n][1]*(m%2)) 
