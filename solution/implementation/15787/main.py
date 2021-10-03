# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/a636cadadf8d444180ee022a5af9353a

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
trains= [0] * (n+1)
commands = []
for _ in range(m):
    commands.append(list(map(int, input().split())))

for command in commands:
    if command[0] == 1:
        _, i, x = command
        trains[i] |= (1 << (x-1)) 
    if command[0] == 2:
        _, i, x = command
        trains[i] &= ~(1 << (x-1))
    if command[0] == 3:
        _, i = command
        trains[i] = trains[i] << 1
        trains[i] &= ((1 << 20) - 1)
    if command[0] == 4:
        _, i = command
        trains[i] = trains[i] >> 1

result = set()
for train in trains[1:]:
    result.add(train)
print(len(result))
