# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/18c3f3c19f314bcba094d2fd49c0c024

import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(n)]

result = 0
for a, b, c in combinations(range(m), 3):
    maxSum = 0
    for i in range(n):
        maxSum += max(like[i][a], like[i][b], like[i][c])
    result = max(result, maxSum)

print(result)
