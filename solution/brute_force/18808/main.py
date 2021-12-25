# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/81188121d759417d8f72e6a00476ce7c

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def rotate(arr, N):
    result  = []
    i_array = []
    j_array = []
    for item in arr:
        i,j = item
        i_array.append(j)
        j_array.append(N-i-1)
        result.append((j,N-i-1))
    i_min = min(i_array)
    j_min = min(j_array)
    real_result = []
    for item in result:
        y,x = item
        real_result.append((y-i_min,x-j_min))
    return real_result

def check(n,m,arr,visit):
    for i in range(n):
        for j in range(m):
            chk = True
            temp = set()
            for y,x in arr:
                if y+i<n and x+j<m:
                    if (y+i,x+j) in visit:
                        chk = False
                        break
                    else:
                        temp.add((y+i,x+j))
                else:
                    chk = False
                    break
            if chk:
                return (True, temp)
    return (False, None)
                
n, m, k = map(int, input().split())
visit = set()
sticker = [] # (max 크기, 스티커들)
for c in range(k):
    a, b = map(int, input().split())
    sticker.append([0, []])
    sticker[c][0] = max(a, b)
    for i in range(a):
        li = list(map(int, input().split()))
        for j in range(b):
            if li[j] == 1:
                sticker[c][1].append((i, j))

q = deque(sticker)
cnt = 0
while q:
    if cnt == 4:
        q.popleft()
        cnt = 0
        continue

    current_sticker = q.popleft()
    M, s = current_sticker
    chk, li = check(n, m, s, visit)
    if chk:
        for i in li:
            visit.add(i)
        cnt=0
        continue
    else:
        q.appendleft((M, rotate(s, M)))
        cnt+=1

print(len(visit))
