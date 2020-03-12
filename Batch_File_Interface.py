import os
from tkinter import Tk, Button, Label, Frame


BatchInterface = Tk()

BatchDirectory = 'D:/Google Drive/Games/Game Saves/2 - Batch Back Up'


for File in os.listdir(BatchDirectory):
    if File.endswith('.bat'):
        print(File)

BatchInterface.mainloop()
