# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/946d652cbd7a4361aaeff5ff1f2612d5
import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
num = [i for i in range(N)]
MIN = 1e9
for i in range(N):
    arr.append(list(map(int, input().split())))
comb_list = list(combinations(num, N//2))
for comb in comb_list:
    start = 0
    link = 0
    remain = [i for i in range(N) if i not in comb]
    for com in combinations(comb, 2):
        start += arr[com[0]][com[1]]
    for ar in combinations(remain, 2):
        link += arr[ar[0]][ar[1]]
    MIN = min(MIN, abs(start - link))
print(MIN)