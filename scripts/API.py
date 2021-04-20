from urllib import request
import ssl

# ProblemNumber : 문제 번호
# ProblemName   : 문제 이름
# ProblemTier   : 문제 난이도 (SolvedAC)
# lastupdate    : 업데이트 로그 (ex 1618947707.736831)

# 
class SolvedAPI:
    def __init__(self):
        self.ssl_context = ssl._create_unverified_context()
        self.cache = dict()

    def request(self):
        pass

    def getProblemName(self, problemID):
        pass
    
