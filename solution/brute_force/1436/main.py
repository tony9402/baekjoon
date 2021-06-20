# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/32ff54d1000b438281226631f054c697
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ct = 0
ans = 0
num = 666

while True:

    if '666' in str(num):
        ct += 1

    if ct == N:
        ans = num
        break

    num += 1

print(ans)