# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/632e2f63fb4a44caacbddb53207f2279
import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
t = k # 미래를 위해 저장
num = list(input())
stack = [] # 정답 저장 및 지울 후보 저장

for i in range(n):
    while k>0 and stack: # 지울 수 있는 숫자가 있을 때
        if stack[-1] < num[i]: # 지우는 게 이득이면
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num[i])

print(*stack[:(n-t)], sep='') #남아있는 숫자는 n-(최초 k) => t를 여기서 사용