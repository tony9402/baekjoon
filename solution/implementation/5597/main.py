# Authored by : samuel95
# Co-authored by : -
# Link : http://boj.kr/5229a16593bd45beb68eefd6224ef63b
import sys

def input():
    return sys.stdin.readline().rstrip()

numbers = [False for _ in range(31)]

for _ in range(28):
    n = int(input())
    numbers[n] = True

ans = []

for i in range(1, 31):
    if not numbers[i]:
        ans.append(i)

print(ans[0])
print(ans[1])
