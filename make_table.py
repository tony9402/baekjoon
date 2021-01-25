import sys

def checkData(data):
    Validate = [ len(i) == 5 for i in data ] # "최소, 최대 2"
    result = False in Validate
    if result:
        print(Validate.index(False))
    return result


def urllevel(name):
    name, number = name.lower()[:-1], name[-1]
    nameDB = [ "bronze", "sliver", "gold", "platinum", "diamond", "ruby"]
    nameDB2 = [ "b", "s", "g", "p", "d", "r" ]
    LEVEL = 0
    if name in nameDB:
        LEVEL = nameDB.index(name)
    else:
        LEVEL = nameDB2.index(name)
    url = f"https://static.solved.ac/tier_small/{LEVEL * 5 + 6 - int(number)}.svg"
    ret = f"<img height=\"25px\" width=\"25px=\" src=\"{url}\"/>"
    return ret

def urlproblem(number, name):
    return f"<a href=\"http://boj.kr/{number}\" target=\"_blank\">{name}</a>"

def urlSolution(url):
    if url == "":
        return ""
    return f"<a href=\"{url}\">바로가기</a>"

class DataForm:
    def __init__(self):
        self.data = { "id": "", "rec": "", "name": "", "level": "", "url": "" }

    def addItem(self, key, value):
        if not key in self.data.keys():
            return True, "Key error"

        self.data[key] = value
        return False, ""
    
    def getItem(self, key):
        if not key in self.data.keys():
            return True, "Key error"
        return False, self.data[key]

    def __lt__(self, other):
        if self.data["rec"] == other.getItem("rec")[1]:
            L = int( self.data["level"][74:][:-7])
            R = int(other.data["level"][74:][:-7])
            return L < R

        return self.data["rec"] != ''
    
    def __repr__(self):
        ID    = self.data["id"]
        REC   = ":heavy_check_mark:" if self.data["rec"] != '' else " "
        NAME  = self.data["name"]
        LEVEL = self.data["level"]
        URL   = self.data["url"]
        PRINT_STR = f"| {ID:02} | {REC:^20} | {NAME:^20} | {LEVEL:^15} | {URL:^20} |"
        return PRINT_STR

class Table:
    title = [ "순번", "추천 문제", "문제 이름", "난이도", "풀이 링크" ]
    keys  = [ "id", "rec", "name", "level", "url" ]
    def __init__(self):
        self.Lines = list()

    def makeForm(self, data):
        # NULL | Not NULL | Not NULL | Not NULL | Not NULL
        ret = dict()
        ret[self.keys[1]] = data[0]
        ret[self.keys[2]] = urlproblem(data[2], data[1])
        ret[self.keys[3]] = urllevel(data[3])
        ret[self.keys[4]] = urlSolution(data[4])

        return ret

    def putLine(self, data):
        if not type(data) == dict:
            return True, "Type Error"
        
        newData = DataForm()
        for k, v in data.items():
            newData.addItem(k, v)
        self.Lines.append(newData)

    def sort(self):
        self.Lines = sorted(self.Lines)
        N = len(self.Lines)
        for i in range(N):
            self.Lines[i].addItem("id", i)
    
    def print(self):
        A,B,C,D,E = self.title
        print(f"| {A:^20} | {B:^20} | {C:^20} | {D:^20} | {E:^20} |")
        print(f"| :-----: | :-----: | :-----: | :-----: | :-----: |")
        N = len(self.Lines)
        for i in range(N):
            print(self.Lines[i])

if __name__=="__main__":
    Input = sys.stdin.readlines()
    data = list()

    # V,N,PN,L,S
    for i in Input:
        Line = list(map(str, i.strip().split(",")))
        NAME = ','.join(Line[:-3][1:])
        Line = Line[:1] + [ NAME ] + Line[-3:]
        data.append(Line)

    # data = [ list(map(str, i.strip().split(","))) for i in Input ]

    # Check Data
    assert(not checkData(data))
    
    outputTable = Table()

    for i in data:
        curLine = outputTable.makeForm(i)
        outputTable.putLine(curLine)

    outputTable.sort()
    outputTable.print()
