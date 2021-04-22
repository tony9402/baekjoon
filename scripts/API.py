from urllib import request
import ssl
import json
import atexit
import time

# ProblemId: 문제 번호
# ProblemName   : 문제 이름
# ProblemTier   : 문제 난이도 (SolvedAC)
# lastupdate    : 업데이트 로그 (ex 1618947707.736831 [minute])

# Database + request
class SolvedAPI:
    def __init__(self, config):
        assert type(config) == dict
        self.ssl_context = ssl._create_unverified_context()
        self.config = config
        self.database = dict()

        # Load Database
        self.__load_database()

        # For saving Database
        atexit.register(self.__save_database)

    def __load_database(self):
        option = "database"
        File = self.config.get(option)

        # Must Be str (string)
        assert type(File) == str, f"[*** Config Error] Not Found {option}, Check config.json"

        with open(File, 'r') as f:
            self.database = json.load(f)
            f.close()

    def __save_database(self):
        option = "testdatabase"
        File = self.config.get(option)

        # Must Be str (string)
        assert type(File) == str, f"[*** Config Error] Not Found {option}, Check config.json"

        with open(File, 'w') as f:
            f.write(json.dumps(self.database, indent=4, ensure_ascii=False))
            f.close()

    # using SolvedAPI
    def __request(self, problemId):
        URL      = f"{self.config['targeturl']}/{self.config['route']['problemid']}{problemId}"
        response = request.urlopen(request.Request(URL), context=self.ssl_context)
        JSON     = json.loads(response.read().decode(self.config.get('encoding')))

        assert JSON.get("success") == True, "[*** API Error] Failed"
        INFO     = JSON["result"]["problems"][0]

        data = {
            "problemId": INFO.get('id'),
            "problemLevel": INFO.get('level'),
            "problemName": INFO.get('title'),
            "average_try": INFO.get('average_try'),
            "solvedtags": list()
        }

        for tag in INFO.get('tags', [ ]):
            solvedtags = dict()
            for config_tags in self.config.get('solvedtags'):
                solvedtags[ config_tags ] = tag[ config_tags ]
            data['solvedtags'].append(solvedtags)

        return data

    # update
    def request(self, problemId):

        # Check problemId Type
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(problemId)}.\n It must be string"

        # information : (in database)
        exist, information = self.getProblemInformation(problemId)
        if exist:
            lastupdate = information.get('lastupdate', 0.0)

            assert type(lastupdate) == float, "[*** Type Error] lastupdate type is {type(lastupdate)}.\n It must be float"
            if lastupdate + self.config.get('update') < time.time():
                return information

        # update
        return self.__request(problemId)

    # update force
    def requestForce(self, problemId):

        # Check ProblemId Type
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(ProblemId)}.\n It must be string"
        return self.__requeset(problemId)

    def getProblemInformation(self, problemId):

        # Check Database
        assert type(problemId) == str, f"[*** Type Error] problemId type is {type(problemId)}.\n It must be string"

        if not problemId in self.database.keys():
            return False, dict()
        
        return True, self.database.get(problemId)

    def saveInformation(self, data):

        # Check data type
        assert type(data) == dict, f"[*** Type Error] data type is {type(data)}.\n It must be dict"

        data['lastupdate'] = time.time()
        problemId = data.get('problemId')
        print(problemId, self.database)
        if problemId in self.database.keys():
            del self.database[problemId]
        self.database.update({problemId: data})

if __name__=="__main__":
    config = dict()
    
    with open("config.json", "r") as f:
        config = json.load(f)
        f.close()
    api = SolvedAPI(config.get("API"))
    data = api.request('1001')
    api.saveInformation(data)
