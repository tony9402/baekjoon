# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/30c745d5f3c547c28e95b5c9a76647c1
import sys

def input():
    return sys.stdin.readline().rstrip()

G = int(input())
P = int(input())
gates = list(range(G + 1))

def find_max(x):
    if gates[x] != x:
        gates[x] = find_max(gates[x])
    return gates[x]

answer = 0
for _ in range(P):
    plane = int(input())
    gate_n = find_max(plane)
    if gate_n == 0:
        print(answer)
        sys.exit(0)
    answer += 1
    gates[gate_n] = gates[gate_n - 1]
print(answer)
