# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/a46811d50ced4e29ad20259b80a37a49

import sys
def input():
    return sys.stdin.readline().rstrip()

board = []
for i in range(19):
    board.append(list(map(int, input().split())))

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            focus = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
                    cnt += 1
                    
                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)
