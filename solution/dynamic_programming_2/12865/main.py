# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/73b9e168131842dd90aa2b02380cb0fa

import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
obj = []
for i in range(n):
    obj.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)] # 초기값으로 아무 물건도 고려하지 않은 경우, 용량이 0인 경우 위해

for num in range(1, n+1): # 모든 물건에 대해
    for weight in range(1, k+1): # 모든 무게에 대해
        if obj[num-1][0] > weight: # 현재 물건을 담지 못하는 경우
            dp[num][weight] = dp[num-1][weight]
        else:
            # 현재 물건을 고려하지 않은 경우, 현재 물건을 담고 이전 물건까지 고려했을 때 담을 수 있는 경우 중 가치가 더 큰 쪽을 선택
            dp[num][weight] = max(dp[num-1][weight], dp[num-1][weight-obj[num-1][0]]+obj[num-1][1])

print(dp[n][k]) # 모든 물건을 고려했을 때 가방 용량 k인 경우 출력
