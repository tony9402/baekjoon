# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/cd4b334129a84bb88708fc8adedc01c5

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
pos = list(input())

cnt = 0
for i in range(n - 1):
    if pos[i] + pos[i + 1] == 'EW':
        cnt += 1

print(cnt)
