from tkinter import *
import random

#global variables
global AnswerBank
names = []
asked = []
score = 0

#colour set
bgc = "#2E5BDE"
tbc = "#FCEDC0"
cbc = "#9FC5E8"

#disctionary containing lists for questions and answers
AnswerBank = {
    1: ["question1","answer1-1","answer1-2","answer1-3","answer1-4","correctanswer",3
    ],
    2: ["question2","answer2-1","answer2-2","answer2-3","answer2-4","correctanswer",3
    ],
    3: ["question3","answer3-1","answer3-2","answer3-3","answer3-4","correctanswer",3
    ],
    4: ["question4","answer4-1","answer4-2","answer4-3","answer4-4","correctanswer",3
    ],
    5: ["question5","answer5-1","answer5-2","answer5-3","answer5-4","correctanswer",3
    ],
    6: ["question6","answer6-1","answer6-2","answer6-3","answer6-4","correctanswer",3
    ],
    7: ["question7","answer7-1","answer7-2","answer7-3","answer7-4","correctanswer",3
    ],
    8: ["question8","answer8-1","answer8-2","answer8-3","answer8-4","correctanswer",3
    ],
    9: ["question9","answer9-1","answer9-2","answer9-3","answer9-4","correctanswer",3
    ],
    10: ["question10","answer10-1","answer10-2","answer10-3","answer10-4","correctanswer",3
    ]
}

#class to control window for questions
class QuizWindow:
  
    def TestProgress(self):
      global score
      ScoreDisplay = self.ScoreLabel
      choice = self.var1.get()
      if len(asked) > 9:
        if choice == AnswerBank[qnum][6]:
          score += 1
          ScoreDisplay.configure(text = score)
          self.QuizInstance.config(text = score)
          #self.EndScreen()
        else:
          print(choice)
          score += 0
          ScoreDisplay.configure(text = "The correct answer was: " + AnswerBank[qnum][5])
          self.QuizInstance.config(text = "Confirm")
          #self.EndScreen()
      else:
        if choice == 0:
          self.QuizInstance.config(text = "Try Again, You didn't select an option")
          choice = self.var1.get()
        else:
          print(choice)
          score += 0
          ScoreDisplay.configure(text = "The correct answer was: " + AnswerBank[qnum][5])
          self.QuizInstance.config(text = "Confirm")

    def __init__(self, parent):

      self.quiz_frame = Frame(parent, bg = bgc, padx = 40, pady = 40)
      self.quiz_frame.grid()

      self.question_label = Label(self.quiz_frame, text = AnswerBank[qnum][0], bg = tbc)
      self.question_label.grid(row = 1, padx = 10, pady = 10)

      self.var1 = IntVar()

      self.rb1 = Radiobutton(self.quiz_frame, text = AnswerBank[qnum][1], bg = bgc, value=1, padx=10, pady=10, variable = self.var1, indicator = 0, background = "light blue")
      self.rb1.grid(row = 2, sticky = W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][2], bg = bgc, value = 2, padx = 10,  pady = 10, variable = self.var1, indicator = 0, background= "light blue")
      self.rb1.grid(row = 3, sticky = W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][3], bg = bgc, value = 3, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
      self.rb1.grid(row = 4, sticky = W)

      self.rb1 = Radiobutton(self.quiz_frame, text=AnswerBank[qnum][4], bg = bgc, value = 4, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
      self.rb1.grid(row = 5, sticky = W)

      self.QuizInstance = Button(self.quiz_frame, text = "Confirm", bg = bgc , command  = self.TestProgress)
      self.QuizInstance.grid(row = 7, padx = 5, pady = 5)

      self.ScoreLabel = Label(self.quiz_frame, text = "Score", bg = bgc)
      self.ScoreLabel.grid(row = 8, padx = 10, pady = 1)

#class to check to make sure the user wants to close the program
class ExitProgram:

  def Cancel(self):
    self.CloseFrame.destroy()
    OpenWindow(root)

  def Confirm(self):
    self.CloseFrame.destroy()
    exit()

  def __init__(self, parent):

    self.CloseFrame = Frame(parent, bg = bgc, padx = 150, pady = 170)
    self.CloseFrame.grid()

    self.ConfirmText = Label(self.CloseFrame, text = "Are you sure?", bg = tbc, borderwidth = 2, relief = "raised", height = 2, width = 20)
    self.ConfirmText.grid(row = 0, pady = 0, padx = 20)

    self.ConfirmButton = Button(self.CloseFrame, text = "Confirm", bg = cbc, command = self.Confirm, width = 10, height = 1)
    self.ConfirmButton.place(x = 110, y = 60)

    self.CancelButton = Button(self.CloseFrame, text = "Cancel", bg = cbc, command = self.Cancel, width = 10, height = 1)
    self.CancelButton.place(x = 0, y = 60)

#class to display players highscores
class HighScorePage:

  def __init__(self, parent):

    self.ScoreFrame = Frame(parent, bg = bgc, padx = 300, pady = 200)
    self.ScoreFrame.grid()

#class to create the home/main window
class OpenWindow:

  def HighscoreOpener(self):
    self.OpenFrame.destroy()
    HighScorePage(root)

  def CloseProgram(self):
    self.OpenFrame.destroy()
    ExitProgram(root)

  def NameList(self):
    name = self.InputBox.get()
    names.append(name)
    print (names)
    self.OpenFrame.destroy()
    QuizWindow(root)

  def __init__(self, parent):

    self.OpenFrame = Frame(parent, bg = bgc, padx = 300, pady = 200)
    self.OpenFrame.grid()

    self.Heading = Label(self.OpenFrame, text = "PlaceHolder", bg = tbc, borderwidth = 2, relief = "raised", height = 3, width = 40)
    self.Heading.place(x = -50, y = -75)

    self.NameInputLabel = Label(self.OpenFrame, text = "Please Enter Your Name", bg = tbc, borderwidth = 2, relief = "raised", height = 2, width = 20)
    self.NameInputLabel.grid(row = 1, padx = 20, pady = 20)

    self.InputBox = Entry(self.OpenFrame)
    self.InputBox.grid(row = 2, padx = 20, pady = 20)

    self.ContinueButton = Button(self.OpenFrame, text = "Play", command = self.NameList, bg = cbc)
    self.ContinueButton.place(width = 75, height = 30, x = 115, y = 140)

    self.HighscoreButton = Button(self.OpenFrame, text = "Highscore", bg = cbc)
    self.HighscoreButton.place(width = 75, height = 30, x = -15, y = 140)
    
    self.ExitButton = Button(self.OpenFrame, text = "Exit", bg = cbc, command = self.CloseProgram)
    self.ExitButton.place(width = 75, height = 30, x = 50, y = 190)

#function to control answer buttons and qustion
def questions_setup(self):
  randomiser()
  self.var1.set(0)
  self.question_label.congfig(text = AnswerBank[qnum][0])
  self.rb1.config(text = AnswerBank[qnum][1])
  self.rb2.config(text = AnswerBank[qnum][2])
  self.rb3.config(text = AnswerBank[qnum][3])
  self.rb4.config(text = AnswerBank[qnum][4])

#function to randomise question order
def randomiser():
  global qnum
  qnum = random.randint(1, 10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

randomiser()

#function to open first window on program launch
if __name__ == "__main__":
  root = Tk() 
  root.title("PlaceHolder")
  MainTab = OpenWindow(root)
  root.mainloop()