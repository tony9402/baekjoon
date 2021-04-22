from API import SolvedAPI
import json

def urlProblem(number, name):
    FORMAT = f"<a href=\"https://www.acmicpc.net/problem/{number}\" target=\"_blank\">{name}</a>"
    return FORMAT

def urlSolution(link):
    if link == "":
        return ""
    FORMAT = f"<a href=\"{link}\">바로가기</a>"
    return FORMAT

def urlLevel(level):
    url = f"https://static.solved.ac/tier_small/{level}.svg"
    ret = f"<img height=\"25px\" width=\"25px\" src=\"{url}\"/>"
    return ret

class DataForm:
    def __init__(self):
        self.data = {
            "id"          : "",
            "rec"         : "",
            "problemId"   : "",
            "name"        : "",
            "level"       : "",
            "url"         : "",
            "average_try" : ""
        }

    def __lt__(self, other):
        if self.data['rec'] == other.getItem('rec'):
            LeftData  = int( self.data['level'][73:][:-7])
            RightData = int(other.data['level'][73:][:-7])
            if LeftData == RightData:
                return self.data['average_try'] < other.data['average_try']
            else:
                return LeftData < RightData

        return self.data['rec'] != ''
    
    def __repr__(self):
        ID         = self.data['id']
        REC        = ":heavy_check_mark:" if self.data['rec'] != "" else " "
        PROBLEMID  = self.data['problemId']
        NAME       = self.data['name']
        LEVEL      = self.data['level']
        URL        = self.data['url']
        FORMATING  = f"| {ID:02} | {REC:^20} | {PROBLEMID:^7} | {NAME:^20} | {LEVEL:^15} | {URL:^20} |"
        return FORMATING
    
    def format(self):
        return self.__repr__()

    def putItem(self, key, value):
        assert key in self.data.keys(), f"[*** Key Error] {key}"
        self.data[key] = value
    
    def getItem(self, key):
        assert key in self.data.keys(), f"[*** Key Error] {key}"
        return self.data[key]


class Table:
    title = [ "순번", "추천 문제", "문제 번호", "문제 이름", "난이도", "풀이 링크" ]
    keys  = [ "id", "rec", "problemId", "name", "level", "url" ]
    
    def __init__(self, api, config):
        self.config = config
        self.api    = api
        self.data   = list()
        self.Line   = list()

    def __read(self, File):

        assert type(File) == str, f"[*** Type Error] File type is {type(File)}.\n It must be str"
        
        self.data = list()
        self.Line = list()

        with open(File, 'r') as f:
            self.data = [ _.strip() for _ in f.readlines() ]
            f.close()
    
    def __write(self, File):

        assert type(File) == str, f"[*** Type Error] File type is {type(File)}.\n It must be str"

        with open(File, 'w') as f:
            f.writelines([ f"{_}\n" for _ in self.data ])
            f.close()

    def __writeREADME(self, tag):
        READMEFile = f"./{tag}/README.md"
        HEADERFile = f"./{tag}/header.md"

        headerData = None
        # Read header
        with open(HEADERFile, 'r') as f:
            headerData = f.readlines()
            f.close()

        # Make New
        with open(READMEFile, 'w') as f:
            f.writelines(headerData)
            f.close()

        # Put Table
        TableFormat = list()
        A,B,C,D,E,F = self.title
        TableFormat.append(f"| {A:^20} | {B:^20} | {C:^20} | {D:^20} | {E:^20} | {F:^20} |\n")
        TableFormat.append(f"| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |\n")
        for line in self.Line:
            TableFormat.append(f"{line.format()}\n")
        with open(READMEFile, 'a+') as f:
            f.writelines(TableFormat)
            f.close()

    def makeForm(self, data, force=False):
        # data -> rec, problemId, solution link
        ret = dict()
        recommend    = data[0]
        problemId    = data[1]
        solutionLink = data[2]
        problemInfo  = dict()
        if force:
            problemInfo = self.api.requestForce(problemId)
        else:
            problemInfo  = self.api.request(problemId)
        problemName  = problemInfo.get('problemName')
        problemLevel = problemInfo.get('problemLevel')

        ret[self.keys[1]] = data[0]
        ret[self.keys[2]] = urlProblem(problemId, problemId)
        ret[self.keys[3]] = urlProblem(problemId, problemName)
        ret[self.keys[4]] = urlLevel(problemLevel)
        ret[self.keys[5]] = urlSolution(solutionLink)

        return ret

    def sort(self):
        self.Line = sorted(self.Line)
        N = len(self.data)
        for i in range(N):
            self.Line[i].putItem("id", i)

    def putLine(self, data):

        assert type(data) == dict, f"[*** Type Error] data type is {type(data)}.\n It must be dict"
        
        newData = DataForm()
        for k, v in data.items():
            newData.putItem(k, v)
        self.Line.append(newData)

    def run(self, force=False):
        
        for tag in self.config.get('tags'):
            self.__read( f"./{tag}/list.md")
            for data in self.data:
                splitData = list(map(str, data.strip().split(',')))
                form = self.makeForm(splitData, force)
                self.putLine(form)

            self.sort()
            self.__writeREADME(tag)
            self.__write(f"{tag}/list.md")

if __name__ == "__main__":
    config = dict()
    with open('./scripts/config.json', 'r') as f:
        config = json.load(f)
        f.close()

    api = SolvedAPI(config.get('API'))
    table = Table(api, config)
    table.run()
