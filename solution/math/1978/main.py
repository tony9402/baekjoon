# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/fba2f023d5c346aa826b3c6922fb0a27
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

prime = [0] * 1005
prime[0] = 1
prime[1] = 1
ct = 0
N = int(input())
arr = list(map(int, input().split()))
for i in range(2, int(sqrt(1005))+1):
    for j in range(i+i, 1005, i):
        if prime[j] == 0:
            prime[j] = 1
for i in arr:
    if not prime[i]:
        ct += 1
print(ct)