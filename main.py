from tkinter import *

global AnswerBank
names = []
asked = []
score = 0

bgc = "#2E5BDE"
tbc = "#FCEDC0"
cbc = "#9FC5E8"

AnswerBank = {
    1: [
    ],
    2: [
    ],
    3: [
    ],
    4: [
    ],
    5: [
    ],
    6: [
    ],
    7: [
    ],
    8: [
    ],
    9: [
    ],
    10: [
    ]
}

class QuizWindow:
    def __init__(self, parent):

      self.quiz_frame = Frame(parent, bg=bgc, padx=40, pady=40)
      self.quiz_frame.grid()

      self.question_label = Label(self.quiz_frame, text=AnswerBank[qnum][0], bg=bgc)
      self.question_label.grid(row=1, padx=10, pady=10)

      self.var1 = IntVar()

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][1], bg=bgc, value=1, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
      self.rb1.grid(row=2, sticky=W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][2], bg=bgc, value=2, padx=10,  pady=10, variable=self.var1, indicator=0, background="light blue")
      self.rb1.grid(row=3, sticky=W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][3], bg=bgc, value=3, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
      self.rb1.grid(row=4, sticky=W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][4], bg=bgc, value=4, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
      self.rb1.grid(row=5, sticky=W)

      self.quiz_instance = Button(self.quiz_frame, text="Confirm", bg=bgc , command  = self.test_progress)
      self.quiz_instance.grid(row=7, padx=5, pady=5)

      self.score_label = Label(self.quiz_frame, text="Score", bg=bgc)
      self.score_label.grid(row=8, padx=10, pady=1)


class OpenWindow:

  def NameList(self):
    name = self.InputBox.get()
    names.append(name)
    print (names)
    self.OpenFrame.destroy()
    QuizWindow(root)

  def __init__(self, parent):

    self.OpenFrame = Frame(parent, bg=bgc, padx=400, pady=180)
    self.OpenFrame.grid()

    self.Heading = Label(self.OpenFrame, text="PlaceHolder", bg=tbc, borderwidth=2, relief="raised")
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