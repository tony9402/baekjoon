#Authored by : shjeong92
#Co-authored by : -
#Link : http://boj.kr/04d943fbb1d14ca0b17c62790a25fe8a
import sys
from itertools import combinations as combi

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
#보드입력받기
board = [list(map(int,input().split())) for _ in range(N)]
#백트래킹용 체크
check = [ [True] * M for _ in range(N)]
#RLUD
dx = (0,0,-1,1)
dy = (1,-1,0,0)
answer = 0
#T 자블록 검색
def block_T(x,y):
    #중앙의 한 점이라고 가정한다
    result = board[x][y]
    # 상하좌우의 티어나온부분 중 날개가 4개면 
    # 제일작은 값을 제거한값이 최대값이 될것이고, 
    # 날개가 2개라면 T가아니고 날개가 3개라면 그냥 그값을 리턴해준다.
    wings = 4
    MIN = int(1e9)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if wings == 2:
            return 0
        #꼬다리부분이 맵을 벗어난다? 그방향 날개는 없는것.
        if not (0<=nx<N and 0<=ny<M):
            wings -= 1
            continue
        #모든 날개 값들을 더해준다.    
        result+= board[nx][ny]
        if MIN > board[nx][ny]:
            MIN = board[nx][ny]
    #모든방향 날개가 살아있단 말이므로 4방향의 날개중 제일 작은날개 하나를 잘라준다.
    if wings == 4:
        result -= MIN
    return result

#T자를 제외한 블록은 dfs를 이용해 계산
def dfs(x,y,val,depth):
    global answer
    if depth == 4:
        answer = max(answer,val)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny]:
                #4개블럭값이 이전 블럭값이면 안되니까 false 해주고
                check[nx][ny] = False
                dfs(nx,ny,val+board[nx][ny],depth+1)
                #끝난후 다시 방문가능처리해줌.
                check[nx][ny] = True


for i in range(N):
    for j in range(M):
        #시작블록을 다시방문하면안됨
        check[i][j] = False
        dfs(i,j,board[i][j],1)
        #끝난후 다시 방문가능처리
        check[i][j] = True

        temp = block_T(i,j)
        answer = max(answer,temp)


print(answer)
