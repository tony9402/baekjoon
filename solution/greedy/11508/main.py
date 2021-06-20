# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/09487b6e14e044f8a477a743e37bce94
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
total = 0

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse = True)

ct = 1

for i in range(N):
    if ct % 3 == 0:
        ct = 1
        continue

    total += arr[i]
    ct += 1

print(total)