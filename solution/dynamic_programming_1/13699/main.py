# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/84dabc0ec83940a9b2ee36e163f602c2
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
t = [0] * (n+4)
t[0] = 1
for i in range(1,n+1):
    for j in range(i):
        t[i] += t[j] * t[i-1-j]
print(t[n])