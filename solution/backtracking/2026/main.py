# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/23aa0efe0fd94f888b47fdcacfbce2c7

import sys

def input():
    return sys.stdin.readline().rstrip()

K, N, F = map(int, sys.stdin.readline().split())
relation = [[True if i == j else False for j in range(N+1)] for i in range(N+1)]

for _ in range(F):
    a, b = map(int, sys.stdin.readline().split())
    relation[a][b] = True
    relation[b][a] = True

def check(cur, friends):  # 지금까지 쌓아온 친구들과 모두 관계가 성립하는지 확인
    result = True
    for friend in friends:
        if not relation[cur][friend]:
            result = False
            break
    return result

def dfs(start, relation, friends):
    global flag, visit, answer
    if flag:  # 친구 관계 성립되면 더이상 할 필요 X
        return
    if len(friends) == K:  # 만족하는 친구관계가 K개 일때
        flag = True
        answer = friends
        return
    for nxt, status in enumerate(relation[start]):
        if not status: continue
        if visit[nxt]: continue
        if not check(nxt, friends): continue
        visit[nxt] = True
        dfs(nxt, relation, friends + [nxt])
        visit[nxt] = False

def solution(relation, K):
    global flag, visit, answer
    flag = False
    answer = -1
    visit = [False for _ in range(N+1)]
    for i in range(1, N+1):
        if sum(relation[i]) < K: continue  # i번째 사람의 친구가 K보다 작으면 할 필요 X
        if flag:  # 성공한 적 있으면 더이상 할 필요 X
            break
        visit[i] = True
        dfs(i, relation, [i])
        visit[i] = False
    return answer

answer = solution(relation, K)

if flag:
    for num in answer:
        print(num)
else:
    print(-1)
