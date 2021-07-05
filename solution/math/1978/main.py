# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/fba2f023d5c346aa826b3c6922fb0a27
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

prime = [1] * 1005
prime[0] = 0
prime[1] = 0
ct = 0
N = int(input())
arr = list(map(int, input().split()))
for i in range(2, int(sqrt(1005))+1):
    for j in range(i+i, 1005, i):
        if prime[j] == 1:
            prime[j] = 0
for i in arr:
    if prime[i]:
        ct += 1
print(ct)
