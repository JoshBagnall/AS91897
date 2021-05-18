from tkinter import *

class OpenWindow:

  def __init__(self, parent):

    self.OpenFrame = Frame(parent, bg=bgc, padx=400, pady=180)
    self.OpenFrame.grid()

    self.Heading = Label(self.OpenFrame, text="PlaceHolder", bg=tbc)
    self.Heading.grid(row=0, padx=20, pady=20)

    self.NameInputLabel = Label(self.OpenFrame, text="Please Enter Your Name", bg=tbc)
    self.NameInputLabel.grid(row=1, padx=20, pady=20)

    self.InputBox = Entry(self.OpenFrame)
    self.InputBox.grid(row=2, padx=20, pady=20)

    self.ContinueButton = Button(self.OpenFrame, text="Continue", command=self.NameList, bg=cbc)
    self.ContinueButton.grid(row=3, padx=20, pady=20)

if __name__ == "__main__":
  root = Tk() 
  root.title("PlaceHolder")
  MainTab = OpenWindow(root)
  root.mainloop()