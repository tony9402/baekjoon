# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/c400c0aa10ea40bc809ad78029ac721d
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
ans = ''
for i in range(N):
    arr.append(input())
for i in range(len(arr[0])):
    ct = 0
    word = arr[0][i]
    for j in range(N):
        if word == arr[j][i]:
            ct += 1
    if ct == N:
        ans += word
    else:
        ans += '?'
print(ans)