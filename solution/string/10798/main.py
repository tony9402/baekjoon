# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/a1c26275e6af44f5a080d54a61b4c677
import sys

def input():
    return sys.stdin.readline().rstrip()

arr = []
ans = ''
max_len = 0
for i in range(5):
    a = input()
    max_len = max(max_len, len(a))
    arr.append(a)

for i in range(max_len):
    for j in range(5):
        if len(arr[j]) <= i:
            continue
        ans += arr[j][i]

print(ans)
