# Authored by : shjeong92
# Co-authored by : -
# Link : http://boj.kr/c6cb199947f24b69ab8c425987c63d1c
import sys
def input():
    return sys.stdin.readline().rstrip()

data = input()
answer = ''
temp=[]
length = len(data)
inParen = False

for i in range(length):
    
    if data[i] == '<':
        inParen = True
    elif data[i] == '>':
        inParen = False
    
    if inParen and data[i] == '<' :
        if temp:
            answer += ''.join(temp[::-1])+'<'
            temp=[]
        else:
            answer +='<'
    elif inParen and data[i] != '<':
        answer += data[i]

    elif not inParen and data[i] =='>':
        answer += data[i]
    
    elif not inParen and data[i]!= ' ':
        temp.append(data[i])
    elif not inParen and data[i]== ' ':
        answer += ''.join(temp[::-1])+' '
        temp=[]

if temp:
    answer+= ''.join(temp[::-1])
print(answer)