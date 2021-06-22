# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/d16fad5335804ed3a30799f0cf9fdf11
import sys

def input():
    return sys.stdin.readline().rstrip()

arr = list(map(int, input().split()))
for i in range(min(arr), 1000001):
    ct = 0
    for j in range(5):
        if i % arr[j] == 0:
            ct += 1
    if ct >= 3:
        print(i)
        break