from urllib import request
import ssl
import json
import atexit
import time
import datetime
import pytz

# ProblemId     : [str]   문제 번호 
# ProblemName   : [str]   문제 이름
# ProblemTier   : [int]   문제 난이도 (SolvedAC)
# lastupdate    : [float] 업데이트 로그 (ex 1618947707.736831 [minute])

def changeLevel(level):
    ALPHA = [ 'B', 'S', 'G', 'P', 'D', 'R' ]
    level -= 1
    return f"{ALPHA[level // 5]}{5 - level % 5}"


# Database + request
class SolvedAPI:
    def __init__(self, config):
        assert type(config) == dict
        self.ssl_context = ssl._create_unverified_context()
        self.config = config
        self.database = dict()
        self.changeLevelLog = list()

        # Load Database
        self.__load_database()
        self.__all_update()

        # For saving Database
        atexit.register(self.__save_database)
        atexit.register(self.__save_change_log)

    def __all_update(self):
        problemList = list()
        problemIds  = list(self.database.keys())
        L = 0
        R = 100
        N = len(problemIds)
        
        while L < N:
            Ids = problemIds[L : R]
            L += 100
            R += 100
            R = min(R, N)

            # 임시, 반드시 업데이트 해야함.
            URL         = f"https://solved.ac/api/v3/problem/lookup?problemIds={','.join(Ids)}"
            req         = request.Request(URL, headers = {'User-Agent': 'Mozilla/5.0'})
            response    = request.urlopen(req, context=self.ssl_context)
            try:
                JSON    = json.loads(response.read().decode(self.config.get('encoding')))
            except:
                assert False, "[*** API Error] Failed"

            for INFO in JSON:
                data = {
                    "problemId":    str(INFO.get('problemId')),   # int -> str
                    "problemLevel": INFO.get('level'),
                    "problemName":  INFO.get('titleKo'),
                    "average_try":  INFO.get('averageTries'),
                    "solvedtags":   list()
                }

                for tag in INFO.get('tags', [ ]):
                    solvedtags = dict()
                    for config_tags in self.config.get('solvedtags'):
                        solvedtags[ config_tags ] = tag[ config_tags ]
                    data['solvedtags'].append(solvedtags)
                self.saveInformation(data)

    def __save_change_log(self):

        if len(self.changeLevelLog) == 0:
            return

        self.changeLevelLog.append('##############################\n')
        with open("./change_level.log", "a+") as f:
            f.writelines(self.changeLevelLog)
            f.close()

    def __load_database(self):
        option = "database"
        File = self.config.get(option)

        # Must Be str (string)
        assert type(File) == str, f"[*** Config Error] Not Found {option}, Check config.json"

        with open(File, 'r') as f:
            self.database = json.load(f)
            f.close()

    def __save_database(self):
        option = "database"
        File = self.config.get(option)

        # Must Be str (string)
        assert type(File) == str, f"[*** Config Error] Not Found {option}, Check config.json"

        with open(File, 'w') as f:
            f.write(json.dumps(self.database, indent=4, ensure_ascii=False))
            f.close()

    # using SolvedAPI
    def __request(self, problemId):
        URL      = f"{self.config['targeturl']}/{self.config['route']['problemid']}{problemId}"
        req      = request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        response = request.urlopen(req, context=self.ssl_context)
        try:
            JSON     = json.loads(response.read().decode(self.config.get('encoding')))
        except:
            assert False, "[*** API Error] Failed"
        INFO     = JSON

        data = {
            "problemId":    str(INFO.get('problemId')),   # int -> str
            "problemLevel": INFO.get('level'),
            "problemName":  INFO.get('titleKo'),
            "average_try":  INFO.get('averageTries'),
            "solvedtags":   list()
        }

        for tag in INFO.get('tags', [ ]):
            solvedtags = dict()
            for config_tags in self.config.get('solvedtags'):
                solvedtags[ config_tags ] = tag[ config_tags ]
            data['solvedtags'].append(solvedtags)

        return data

    # lazy update
    def request(self, problemId):

        if type(problemId) == int:
            problemId = str(problemId)

        # Check problemId Type
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(problemId)}.\n It must be string"

        # information : (in database)
        exist, information = self.getProblemInformation(problemId)
        if exist:
            lastupdate = information.get('lastupdate', 0.0)

            assert type(lastupdate) == float, "[*** Type Error] lastupdate type is {type(lastupdate)}.\n It must be float"
            
            timestamp = datetime.datetime.now(pytz.timezone('Asia/Seoul')).timestamp()
            if lastupdate + self.config.get('update') > timestamp:
                return information

        # update
        newData = self.__request(problemId)
        self.saveInformation(newData)
        return newData

    # update force
    def requestForce(self, problemId):

        if type(problemId) == int:
            problemId = str(problemId)

        # Check ProblemId Type
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(ProblemId)}.\n It must be string"
        # newData = self.__request(problemId)
        newData = self.request(problemId)

        exist, information = self.getProblemInformation(problemId)

        update    = False
        updateLog = ""
        if exist:
            beforeLevel = information.get('problemLevel')
            newLevel    = newData.get('problemLevel')
            if beforeLevel != newLevel:
                updateLog = f"[{problemId}] {changeLevel(beforeLevel)} -> {changeLevel(newLevel)} https://www.acmicpc.net/problem/{problemId}"
                update = True
        else:
            updateLog = f"[{problemId}] Not Exist -> {changeLevel(newLevel)} https://www.acmicpc.net/problem/{problemId}"
            update = True

        if update:
            self.changeLevelLog.append(f"{updateLog}\n")

        self.saveInformation(newData)
        return newData

    def getProblemInformation(self, problemId):

        if type(problemId) == int:
            problemId = str(problemId)

        # Check Database
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(problemId)}.\n It must be string"

        if not problemId in self.database.keys():
            return False, dict()
        
        return True, self.database.get(problemId)

    def saveInformation(self, data):

        # Check data type
        assert type(data) == dict, f"[*** Type Error] data type is {type(data)}.\n It must be dict"

        timestamp = datetime.datetime.now(pytz.timezone('Asia/Seoul')).timestamp()
        data['lastupdate'] = timestamp
        problemId = data.get('problemId')

        if problemId in self.database.keys():
            del self.database[problemId]
        self.database.update({problemId: data})

# Example
if __name__=="__main__":
    config = dict()
    with open("config.json", "r") as f:
        config = json.load(f)
        f.close()
    api = SolvedAPI(config.get("API"))
    data = api.request('1001')
    api.saveInformation(data)
