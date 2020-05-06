import json

class LevelReader:
    """ Code to read in levels """
    
    def readInLevel(self, levelToRead):
        with open('./levels/'+levelToRead) as json_file:
            try:                
                return json.load(json_file)
            except ValueError as e:
                print("Invalid Json for level: " + levelToRead)
                quit()            
