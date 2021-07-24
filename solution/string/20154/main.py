# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/ff79a90b0e024c4eb328a8595918b096
import sys

def input():
    return sys.stdin.readline().rstrip()

DB = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
dic = {}
for idx, data in enumerate(DB):
    dic[chr(idx+65)] = DB[idx] # 'A' : 65

total = 0
a = input()
for i in a:
    total += dic[i]
total = total % 10
if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
