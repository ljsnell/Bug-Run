import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Level_Selector:

    def lvlSelector(self):
        Tk().withdraw()
        filename = askopenfilename()
        path = filename.split('/')
        return path[-1]
