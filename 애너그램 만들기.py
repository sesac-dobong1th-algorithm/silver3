# collections.Counter 활용 코드
from collections import Counter

c1, c2 = Counter(str1 := input()), Counter(str2 := input())
print(((c1 | c2) - (c1 & c2)).total())


# 공통 문자 치환으로 없앤 코드
str1, str2 = input(), input()
for s in str1:
    if s in str2:
        str1, str2 = str1.replace(s, "", 1), str2.replace(s, "", 1)
print(len(str1 + str2))


# str.count 활용 코드
str1, str2 = input(), input()
common_str = set(str1) & set(str2)
print(
    len(str1)
    + len(str2)
    - 2 * sum(min(str1.count(s), str2.count(s)) for s in common_str)
)
