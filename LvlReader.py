import json
import os
import sys

class LevelReader:
    """ Code to read in levels """
    
    def readInLevel(self, levelToRead):
        levelPath = './levels/'+levelToRead

        # Ensure lvl is smaller than 1 GB
        if os.stat(levelPath).st_size < 1073741824:
            with open(levelPath) as json_file:
                try:                
                    return json.load(json_file)
                except ValueError as e:
                    print("Invalid Json for level: " + levelToRead)
                    sys.exit()            
        else:
            print("Level file is too big!")
            sys.exit()
