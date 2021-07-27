# Authored by : samuel95
# Co-authored by : -
# Link : http://boj.kr/56db895ff06047bb8d3cea233a924472
import sys, math

def input():
    return sys.stdin.readline().rstrip()

def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
        return True
    elif a < b:
        parent[b] = a
        return True
    return False

n = int(input())

# 별들의 좌표를 넣어준다.
stars = []
for i in range(n):
    x,y = map(float,input().split())
    stars.append([x,y])
    
# MST 활용을 위해 (거리,시작,끝)을 만든다.
parent = [i for i in range(n+1)]
edges = []
for i in range(n-1):
    for j in range(i+1,n):
        start = stars[i]
        end = stars[j]
        distance = math.sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)
        edges.append([distance,i,j])

edges.sort()

cnt, ans = 0,0

# Union Find
for edge in edges:
    if union(parent, edge[1], edge[2]):
        ans += edge[0]
        cnt += 1
        if cnt == n - 1:
            break

print(round(ans,2))
