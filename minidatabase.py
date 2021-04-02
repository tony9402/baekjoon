import os
import json
import ssl
import argparse
from urllib import request

# Custom Problem Database
class Database:
    DB = dict()
    def __init__(self):
        self.ssl_context = ssl._create_unverified_context()
        self.readDB()

    def readDB(self, file="database.json"):
        with open(file, 'r') as f:
            self.DB = json.load(f)
            f.close()
    
    def saveDB(self, file="database.json"):
        with open(file, 'w') as f:
            f.write(json.dumps(self.DB, indent=4, ensure_ascii=False))
            f.close()

    def itol(self, level): ## Only Bronze ~ Platinum in my workbook
        NAME  = [ 'B', 'S', 'G', 'P', 'D' ]
        NUMB  = [   1,   2,   3,   4,   5 ]
        LEFT  = NAME[ (level - 1) // 5 ]
        RIGHT = NUMB[ 4 - (level - 1) % 5 ]
        return f"{LEFT}{RIGHT}"

    def __getProblemInfo(self, problemID):
        print(f"API {problemID}")
        url   = f"https://api.solved.ac/v2/problems/show.json?id={problemID}"
        res   = request.urlopen(request.Request(url), context=self.ssl_context)
        JSON  = json.loads(res.read().decode('UTF-8'))
        LEVEL = self.itol(JSON["result"]["problems"][0]["level"])
        NAME  = JSON["result"]["problems"][0]["title"]
        return {
            "id": problemID,
            "level": LEVEL,
            "name": NAME
        }

    def add(self, problemID):
        if type(problemID) == int:
            problemID = str(problemID)

        if problemID in self.DB.keys():
            return 

        info = self.__getProblemInfo(problemID)
        self.DB[problemID] = info

    def getInfo(self, problemID):
        if problemID in self.DB.keys():
            return self.DB[problemID]
        self.add(problemID)
        return self.DB[problemID]

    # update all
    def updateLevel(self):
        for problemID in self.DB.keys():
            info = self.__getProblemInfo(problemID)
            if self.DB[problemID]["level"] == info["level"]:
                continue
            
            pre_level = self.DB[problemID]["level"]
            nxt_level = info["level"]
            self.DB[problemID]["level"] = info["level"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser("database update")
    arg    = parser.add_argument

    arg('--level', dest="updateLevel", action="store_true")
    parser.set_defaults(updateLevel=False)

    args = parser.parse_args()

    db = Database()
    if args.updateLevel:
        db.updateLevel()
        db.saveDB()
