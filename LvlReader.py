import json

class LevelReader:
    """ Code to read in levels """
    
    def readInLevel(self, levelToRead):
        with open('./levels/'+levelToRead+'.json') as json_file:        
            return json.load(json_file)
