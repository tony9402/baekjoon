# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e743b059cab14671bad3e38466447009

import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1): # 재료를 i개 뽑을 때
    lst = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

    for food in lst: # 경우 하나씩 탐색
        s = 1
        b = 0
        for j in range(i): # 맛 계산
            s *= sour[food[j]]
            b += bitter[food[j]]
        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)
