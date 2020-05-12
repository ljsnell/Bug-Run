import unittest
import sys
import lvl_reader

class TestLevelReader(unittest.TestCase):
    
    def testReadInLevel(self):
        result = lvl_reader.LevelReader().readInLevel('level1')        
        self.assertEqual(len(result), 2)
