import unittest
import sys
import LvlReader

class TestLevelReader(unittest.TestCase):
    
    def testReadInLevel(self):
        result = LvlReader.LevelReader().readInLevel('level1')
        print(result)
