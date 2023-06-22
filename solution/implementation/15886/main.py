# Authored by : hyeonjaee
# Co-authored by : -
# Link : http://boj.kr/f9cd00a87d59430abd180cfe4050d394
import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
board = input()
ans = sum(1 for i in range(n-1) if board[i] == 'E' and board[i+1] == 'W')
print(ans)