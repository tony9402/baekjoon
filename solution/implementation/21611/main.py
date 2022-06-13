# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/806a6fecac8942468b31c6cd4ed5af73

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
g_map = [list(map(int, input().split())) for _ in range(n)]
oper = [list(map(int, input().split())) for _ in range(m)]
sol = [0, 0, 0]

def linear(g_map, n):
    #회오리 모양으로 저장된 걸
    #일자형 리스트로 변환
    x, y, num = n//2, n//2, n//2
    lst = []
    
    for i in range(num):
        x -= 1
        lst.append(g_map[y][x])
        
        num_down = i*2 + 1
        for _ in range(num_down):
            y += 1
            lst.append(g_map[y][x])
            
        for _ in range(num_down+1):
            x += 1
            lst.append(g_map[y][x])
        
        for _ in range(num_down+1):
            y -= 1
            lst.append(g_map[y][x])
        
        for _ in range(num_down+1):
            x -= 1
            lst.append(g_map[y][x])

    return lst

def blizard(n):
    #서남동북 방향으로 블리자드 발동 시 
    #지워지는 구슬 번호 저장
    num = n//2
    lst = [[], [], [], []]
    
    pos = 0
    cnt = 0
    for i in range(num):
        cnt += 1
        pos += cnt
        lst[0].append(pos)
        cnt += 1
        for j in range(1, 4):
            pos += cnt
            lst[j].append(pos)
    
    return lst


l_map = linear(g_map, n)
b_area = blizard(n)

#문제에서 주어지는 방향와 맞도록 변경
dir_m = [3, 1, 0, 2]
for i in range(m):  
    dir, length = dir_m[oper[i][0]-1], oper[i][1]
    
    #블리자드 발동
    del_idx = b_area[dir][:length]

    #블리자드 맞은 구슬 빼고 나머지 구슬 이동
    tmp = l_map[:del_idx[0]-1]
    for i in range(len(del_idx)-1):
        tmp += l_map[del_idx[i]:del_idx[i+1]-1]
    tmp += l_map[del_idx[-1]:]
    
    l_map = tmp
    
    #구슬 폭발 단계
    while True:
        idx = 0
        explode_lst = []
        while idx < len(l_map):
            if l_map[idx] == 0 or idx == len(l_map)-1: #빈 칸
                break
            
            if l_map[idx] == l_map[idx+1]: #연속한다?
                start = idx
                idx += 1
                while idx < len(l_map) and l_map[idx-1] == l_map[idx]:
                        idx += 1
                #l_map[start:idx] 구간 날려야 함(len>=4)
                if idx - start >= 4:
                    explode_lst.append([start, idx])
                    sol[l_map[start]-1] += (idx-start)
            
            else:
                idx += 1
                
        if explode_lst: #폭발하는 구슬이 있으면
            #폭발한 구슬 제외하고 구슬 이동
            tmp = l_map[:explode_lst[0][0]]
            for i in range(len(explode_lst)-1):
                tmp += l_map[explode_lst[i][1]:explode_lst[i+1][0]]
            tmp += l_map[explode_lst[-1][1]:]
            l_map = tmp
        else: #폭발하는 구슬이 없으면 phase 종료
            break
    
    #구슬 변화 단계
    new_map = []
    idx = 0
    cnt = 0
    while idx < len(l_map) and cnt < n*n-1:
        if l_map[idx] == 0:
            break
        
        if idx != len(l_map)-1 and l_map[idx] == l_map[idx+1]: #연속한다?
            start = idx
            idx += 1
            while idx < len(l_map) and l_map[idx-1] == l_map[idx]:
                    idx += 1
            new_map.append(idx-start)
            new_map.append(l_map[start])
            cnt += 2
            
        else:
            new_map.append(1)
            new_map.append(l_map[idx])
            cnt += 2
            idx += 1
                
    l_map = new_map

print(sol[0]+sol[1]*2+sol[2]*3)