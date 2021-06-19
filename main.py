#Importing neccesary fucntion
from tkinter import *
import random

#global variables.
global answer_bank
names = []
asked = []
score = 0

#colour set.
bgc = "#2E5BDE"
tbc = "#FCEDC0"
cbc = "#9FC5E8"

#disctionary containing lists for questions and answers.
answer_bank = {
    1: ["What is the correct formula for calculating speed", "Δa/Δt", "Δv/Δt", "Δd/Δt", "Δt/Δd", "Δd/Δt", 3
    ],
    2: ["How do you calculate momentum", "answer2-1", "answer2-2", "answer2-3", "answer2-4", "answer2-3", 3
    ],
    3: ["What is velocity", "A vector quantity", "A scalar quantity", "A measurement of time", "answer3-4", "A vector quantity", 1
    ],
    4: ["question4", "answer4-1", "answer4-2", "answer4-3", "answer4-4", "answer4-3", 3
    ],
    5: ["question5", "answer5-1", "answer5-2", "answer5-3", "answer5-4", "answer5-3", 3
    ],
    6: ["question6", "answer6-1", "answer6-2", "answer6-3", "answer6-4", "answer6-3", 3
    ],
    7: ["question7", "answer7-1", "answer7-2", "answer7-3", "answer7-4", "answer7-3", 3
    ],
    8: ["question8", "answer8-1", "answer8-2", "answer8-3", "answer8-4", "answer8-3", 3
    ],
    9: ["question9", "answer9-1", "answer9-2", "answer9-3", "answer9-4", "answer9-3", 3
    ],
    10: ["question10", "answer10-1", "answer10-2", "answer10-3", "answer10-4", "answer10-3", 3
    ]
}

#class to control window for questions.
class QuizWindow:

    #function to make answer buttons and question text box update with each new question.
    def question_setup(self):
      randomiser()
      self.choice_variable.set(0)
      self.question_label.config(text  = answer_bank[qnum][0])
      self.answer1.config(text = answer_bank[qnum][1])
      self.answer2.config(text = answer_bank[qnum][2])
      self.answer3.config(text = answer_bank[qnum][3])
      self.answer4.config(text = answer_bank[qnum][4])
      self.quiz_continue.config(text = "Confirm")

    #function to check if the user has inputted the correct answer, manage score, and progress questions.
    def test_progress(self):
      global score
      score_display = self.score_label
      choice = self.choice_variable.get()
      if len(asked) > 9:
        if choice == answer_bank[qnum][6]:
          score += 1
          score_display.configure(text = score)
          #self.EndScreen()
        else:
          print(choice)
          score += 0
          score_display.configure(text = "The correct answer was: " + answer_bank[qnum][5])
          self.quiz_continue.config(text = "Confirm")
          #self.EndScreen()
      else:
        if choice == 0:
          self.quiz_continue.config(text = "Try Again, You didn't select an option")
          choice = self.choice_variable.get()
        else:
          if choice == answer_bank[qnum][6]:
            score += 1
            score_display.configure(text = score)
            self.question_setup()
          else:
            print(choice)
            score += 0
            score_display.configure(text = "The correct answer was: " + answer_bank[qnum][5])
            self.quiz_continue.config(text = "Confirm")
            self.question_setup()

    #function to create window for questions and answers.
    def __init__(self, parent):

      self.quiz_frame = Frame(parent, bg = background_colour, padx = 150, pady = 170)
      self.quiz_frame.grid()

      self.question_label = Label(self.quiz_frame, text = answer_bank[qnum][0], bg = text_box_colour, borderwidth = 2, relief = "raised", height = 3, width = 40)
      self.question_label.grid(row = 1, padx = 10, pady = 10)

      self.choice_variable = IntVar()

      self.radio_button1 = Radiobutton(self.quiz_frame, bg = button_colour, value = 1, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button1.grid(row = 2, sticky = W, pady = 3)

      self.answer1 = Label(text = answer_bank[qnum][1], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer1.place(width = 200, height = 40, x = 250, y = 242)

      self.radio_button2 = Radiobutton(self.quiz_frame, bg = button_colour, value = 2, padx = 10,  pady = 10, variable = self.choice_variable)
      self.radio_button2.grid(row = 3, sticky = W, pady = 3)

      self.answer2 = Label(text = answer_bank[qnum][2], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer2.place(width = 200, height = 40, x = 250, y = 292)

      self.radio_button3 = Radiobutton(self.quiz_frame, bg = button_colour, value = 3, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button3.grid(row = 4, sticky = W, pady = 3)

      self.answer3 = Label(text = answer_bank[qnum][3], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer3.place(width = 200, height = 40, x = 250, y = 342)

      self.radio_button4 = Radiobutton(self.quiz_frame, bg = button_colour, value = 4, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button4.grid(row = 5, sticky = W, pady = 3)

      self.answer4 = Label(text = answer_bank[qnum][4], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer4.place(width = 200, height = 40, x = 250, y = 392)

      self.quiz_continue = Button(self.quiz_frame, text = "Confirm", bg = button_colour , command  = self.test_progress)
      self.quiz_continue.grid(row = 7, padx = 5, pady = 10)

      self.score_label = Label(self.quiz_frame, text = "Score", bg = background_colour)
      self.score_label.grid(row = 8, padx = 10, pady = 1)


#class to check to make sure the user wants to close the program
class ExitProgram:

  def Cancel(self):
    self.close_frame.destroy()
    OpenWindow(root)

  def Confirm(self):
    self.close_frame.destroy()
    exit()

  def __init__(self, parent):

    self.close_frame = Frame(parent, bg = bgc, padx = 150, pady = 170)
    self.close_frame.grid()

    self.confirm_text = Label(self.close_frame, text = "Are you sure?", bg = tbc, borderwidth = 2, relief = "raised", height = 2, width = 20)
    self.confirm_text.grid(row = 0, pady = 0, padx = 20)

    self.confirm_button = Button(self.close_frame, text = "Confirm", bg = cbc, command = self.Confirm, width = 10, height = 1)
    self.confirm_button.place(x = 110, y = 60)

    self.cancel_button = Button(self.close_frame, text = "Cancel", bg = cbc, command = self.Cancel, width = 10, height = 1)
    self.cancel_button.place(x = 0, y = 60)

#class to create the home/main window
class OpenWindow:

  def CloseProgram(self):
    self.open_frame.destroy()
    ExitProgram(root)

  def NameList(self):
    name = self.input_box.get()
    names.append(name)
    print (names)
    self.open_frame.destroy()
    QuizWindow(root)

  def __init__(self, parent):

    self.open_frame = Frame(parent, bg = bgc, padx = 300, pady = 200)
    self.open_frame.grid()

    self.heading = Label(self.open_frame, text = "PlaceHolder", bg = tbc, borderwidth = 2, relief = "raised", height = 3, width = 40)
    self.heading.place(x = -50, y = -75)

    self.name_input_label = Label(self.open_frame, text = "Please Enter Your Name", bg = tbc, borderwidth = 2, relief = "raised", height = 2, width = 20)
    self.name_input_label.grid(row = 1, padx = 20, pady = 20)

    self.input_box = Entry(self.open_frame)
    self.input_box.grid(row = 2, padx = 20, pady = 20)

    self.continue_button = Button(self.open_frame, text = "Play", command = self.NameList, bg = cbc)
    self.continue_button.place(width = 75, height = 30, x = 115, y = 140)

    self.highscore_button = Button(self.open_frame, text = "Highscore", bg = cbc)
    self.highscore_button.place(width = 75, height = 30, x = -15, y = 140)
    
    self.exit_button = Button(self.open_frame, text = "Exit", bg = cbc, command = self.CloseProgram)
    self.exit_button.place(width = 75, height = 30, x = 50, y = 190)

#function to control answer buttons and qustion
def questions_setup(self):
  randomiser()
  self.var1.set(0)
  self.question_label.congfig(text = answer_bank[qnum][0])
  self.rb1.config(text = answer_bank[qnum][1])
  self.rb2.config(text = answer_bank[qnum][2])
  self.rb3.config(text = answer_bank[qnum][3])
  self.rb4.config(text = answer_bank[qnum][4])

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
  main_tab = OpenWindow(root)
  root.mainloop()