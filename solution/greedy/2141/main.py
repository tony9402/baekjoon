# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/8be8b254ebe24830805a22953bdb3fcc
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)] 
lst.sort() # 마을 위치 따라 먼저 정렬

dist = 0
r_man, l_man = 0, 0
for i in range(n):
    tmp = lst[i][0] - lst[0][0]
    dist += tmp*lst[i][1] # (최초 마을 ~ i번째 마을 거리) * 사람 수
    r_man += lst[i][1] #현재 위치보다 오른똑에 있는 사람 수

min_dist = dist
sol = lst[0][0]
for i in range(1, n):
    tmp = lst[i][0] - lst[i-1][0]
    l_man += lst[i-1][1] # 이동 시 왼쪽에 있게 될 사람 추가
    r_man -= lst[i-1][1] # 이동 시 더 이상 오른쪽에 있지 않는 사람 제거
    dist = dist + (l_man - r_man)*tmp # 거리 계산
    
    if min_dist > dist: #업데이트
        min_dist = dist
        sol = lst[i][0]

print(sol)
