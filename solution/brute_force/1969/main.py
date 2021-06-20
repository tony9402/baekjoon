# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/c08f03602f524dc3822344da70739929

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = []
word = ''
dist = 0

for i in range(N):
    arr.append(input())

for i in range(M):
    dic = {}
    for j in range(N):
        if arr[j][i] not in dic:
            dic[arr[j][i]] = 1

        else:
            dic[arr[j][i]] += 1

    ans = list(dic.items())
    ans.sort(key = lambda x : (-x[1], x[0]))
    word += ans[0][0]
    dist += N - ans[0][1]

print(word)
print(dist)