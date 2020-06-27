import os
from tkinter import Tk, Button, Label, Frame

Background = 'LightSteelBlue1'
BoldBaseFont = "Arial Bold"
BaseFont = "Arial"
FontColor = "Black"

BatchInterface = Tk()
BatchInterface.title("Batch File Interface")
BatchInterface.geometry("400x500")
# BatchInterface.iconbitmap('Fireball Icon.ico')
BatchInterface.configure(bg=Background)

BatchDirectory = 'D:/Google Drive/Games/Game Saves/2 - Batch Back Up'

BatchList = []
RowCounter = 0

for File in os.listdir(BatchDirectory):
    if File.endswith('.bat'):
        print(File)
        BatchList.append(Button(BatchInterface))
        BFile.config(text=File)
        BFile.grid(column=0, row=RowCounter + 1)
        RowCounter += 1

for button in BatchList:
    button.config(text="Use Level "+str(RowCounter+1) + " Spell", font=(BaseFont, 15), command=partial(SpellUsedButton, (RowCounter + 1)))
    button.grid(column=1, row=RowCounter + 2, pady=5, padx=(4, 20))


BatchInterface.mainloop()
