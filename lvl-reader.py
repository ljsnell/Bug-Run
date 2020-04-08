import json

class LevelReader:
    """ Code to read in levels """
    
    def readInLevel(self, levelToRead):
        return json.load('./levels/'+levelToRead+".json")
