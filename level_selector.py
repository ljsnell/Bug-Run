from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Level_Selector:

    def lvlSelector(self):
        print("In lvl selector")
        Tk().withdraw()
        filename = askopenfilename()
        print(filename)
        return filename
