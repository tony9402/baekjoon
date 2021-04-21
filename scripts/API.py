from urllib import request
import ssl
import json
import atexit

# ProblemId: 문제 번호
# ProblemName   : 문제 이름
# ProblemTier   : 문제 난이도 (SolvedAC)
# lastupdate    : 업데이트 로그 (ex 1618947707.736831)

# Database + request
class SolvedAPI:
    def __init__(self, config):
        assert type(config) == dict
        self.ssl_context = ssl._create_unverified_context()
        self.config = config
        self.database = dict()

        self.__load_database()
        atexit.register(self.__save_database)

    def __load_database(self):
        file = self.config.get("database")
        assert type(file) == str
        with open(file, 'r') as f:
            self.database = json.load(f)
            f.close()

    def __save_database(self):
        # file = self.config.get("database")
        file = self.config.get('testdatabase')
        assert type(file) == str
        with open(file, 'w') as f:
            f.write(json.dumps(self.database, indent=4, ensure_ascii=False))
            f.close()

    def request(self):
        pass

    def getProblemName(self, problemId):
        pass

if __name__=="__main__":
    config = dict()
    
    with open("config.json", "r") as f:
        config = json.load(f)
        f.close()
    api = SolvedAPI(config.get("API"))
    print(dir(api))
