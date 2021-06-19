#Importing neccesary fucntion
from tkinter import *
import random

#global variables.
global answer_bank
names = []
asked = []
score = 0

#colour set.
background_colour = "#2E5BDE"
text_box_colour = "#FCEDC0"
button_colour = "#9FC5E8"

#disctionary containing lists for questions and answers.
answer_bank = {
    1: ["What is the correct formula for calculating speed?", "s = Δa/Δt", "s = Δv/Δt", "s = Δd/Δt", "s = Δt/Δd", "s = Δd/Δt", 3
    ],
    2: ["How do you calculate momentum?", "Force x distance", "Mass x velocity", "Mass x acceleration", "Velocity / radius", "Mass x velocity", 2
    ],
    3: ["What is velocity?", "A vector quantity", "A scalar quantity", "A measurement of time", "The same as Speed", "A vector quantity", 1
    ],
    4: ["What is the value of g?", "12m/s", "9.8Km/h", "3.6m/s", "9.8m/s", "9.8m/s", 4
    ],
    5: ["What is the formula for torque?", "t = mv", "t = -kx", "t = Fd", "t = FΔt", "t = Fd", 3
    ],
    6: ["What is net force?", "The forwards force is the greatest", "The force a net has", "All forces on an object are negative", "All forces on an object equal 0", "All forces on an object equal 0", 4
    ],
    7: ["What is work?", "Force x distance", "Force / time", "Mass x Accerlation", "The place you go to get money", "Force x distance", 1
    ],
    8: ["What is the formula for power?", "P = W/t", "P = Fd", "P = 1/2mv2", "P = ma", "P = W/t", 1
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
      if len(asked) > 7:
        if choice == answer_bank[qnum][6]:
          score += 1
          score_display.configure(text = score)
          self.quiz_frame.destroy()
          EndScreen(root)
        else:
          print(choice)
          score += 0
          score_display.configure(text = "The correct answer was: " + answer_bank[qnum][5])
          self.quiz_continue.config(text = "Confirm")
          self.quiz_frame.destroy()
          EndScreen(root)
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

      self.quiz_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
      self.quiz_frame.grid()

      self.question_label = Label(self.quiz_frame, text = answer_bank[qnum][0], background = text_box_colour, borderwidth = 2, relief = "raised", height = 3, width = 40)
      self.question_label.grid(row = 1, padx = 10, pady = 10)

      self.choice_variable = IntVar()

      #radiobutton and answer group 1
      self.radio_button1 = Radiobutton(self.quiz_frame, background = button_colour, value = 1, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button1.grid(row = 2, sticky = W, pady = 3)

      self.answer1 = Label(text = answer_bank[qnum][1], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer1.place(width = 200, height = 40, x = 250, y = 242)

      #radiobutton and answer group 2
      self.radio_button2 = Radiobutton(self.quiz_frame, background = button_colour, value = 2, padx = 10,  pady = 10, variable = self.choice_variable)
      self.radio_button2.grid(row = 3, sticky = W, pady = 3)

      self.answer2 = Label(text = answer_bank[qnum][2], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer2.place(width = 200, height = 40, x = 250, y = 292)

      #radiobutton and answer group 3
      self.radio_button3 = Radiobutton(self.quiz_frame, background = button_colour, value = 3, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button3.grid(row = 4, sticky = W, pady = 3)

      self.answer3 = Label(text = answer_bank[qnum][3], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer3.place(width = 200, height = 40, x = 250, y = 342)

      #radiobutton and answer group 4
      self.radio_button4 = Radiobutton(self.quiz_frame, background = button_colour, value = 4, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button4.grid(row = 5, sticky = W, pady = 3)

      self.answer4 = Label(text = answer_bank[qnum][4], background = button_colour, borderwidth = 2, relief = "raised")
      self.answer4.place(width = 200, height = 40, x = 250, y = 392)

      self.quiz_continue = Button(self.quiz_frame, text = "Confirm", background = button_colour , command  = self.test_progress)
      self.quiz_continue.grid(row = 7, padx = 5, pady = 10)

      self.score_label = Label(self.quiz_frame, text = "Score", background = background_colour)
      self.score_label.grid(row = 8, padx = 10, pady = 1)

#class to show endsceen with options to close program and play again
class EndScreen:

  def PlayAgain(self):
    self.final_frame.destroy()
    OpenWindow(root)

  def Leave(self):
    self.final_frame.destroy()
    ExitProgram(root)

  def __init__(self, parent):

    self.final_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
    self.final_frame.grid()

    self.ending_text = Label(self.final_frame, text = "Well done, you got {} out of 8 questions right" .format(score), background = text_box_colour, borderwidth = 2, relief = "raised", height = 2, width = 50)
    self.ending_text.grid(row = 0, pady = 0, padx = 20)

    self.play_again_button = Button(self.final_frame, text = "Play Again?", background = button_colour, command = self.PlayAgain, width = 12, height = 1)
    self.play_again_button.place(x = 210, y = 60)

    self.leave_button = Button(self.final_frame, text = "Exit", background = button_colour, command = self.Leave, width = 12, height = 1)
    self.leave_button.place(x = 80, y = 60)

#class to check to make sure the user wants to close the program
class ExitProgram:

  def Cancel(self):
    self.close_frame.destroy()
    OpenWindow(root)

  def Confirm(self):
    self.close_frame.destroy()
    exit()

  def __init__(self, parent):

    self.close_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
    self.close_frame.grid()

    self.confirm_text = Label(self.close_frame, text = "Are you sure you want to exit?", background = text_box_colour, borderwidth = 2, relief = "raised", height = 2, width = 30)
    self.confirm_text.grid(row = 0, pady = 0, padx = 20)

    self.confirm_button = Button(self.close_frame, text = "Confirm", background = button_colour, command = self.Confirm, width = 10, height = 1)
    self.confirm_button.place(x = 140, y = 60)

    self.cancel_button = Button(self.close_frame, text = "Cancel", background = button_colour, command = self.Cancel, width = 10, height = 1)
    self.cancel_button.place(x = 30, y = 60)

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

    self.open_frame = Frame(parent, background = background_colour, padx = 300, pady = 200)
    self.open_frame.grid()

    self.heading = Label(self.open_frame, text = "PlaceHolder", background = text_box_colour, borderwidth = 2, relief = "raised", height = 3, width = 40)
    self.heading.place(x = -50, y = -75)

    self.name_input_label = Label(self.open_frame, text = "Please Enter Your Name", background = text_box_colour, borderwidth = 2, relief = "raised", height = 2, width = 20)
    self.name_input_label.grid(row = 1, padx = 20, pady = 20)

    self.input_box = Entry(self.open_frame)
    self.input_box.grid(row = 2, padx = 20, pady = 20)

    self.continue_button = Button(self.open_frame, text = "Play", command = self.NameList, background = button_colour)
    self.continue_button.place(width = 75, height = 30, x = 50, y = 140)
    
    self.exit_button = Button(self.open_frame, text = "Exit", background = button_colour, command = self.CloseProgram)
    self.exit_button.place(width = 75, height = 30, x = 50, y = 190)

#function to control answer buttons and qustion
def questions_setup(self):
  randomiser()
  self.choice_variable.set(0)
  self.question_label.congfig(text = answer_bank[qnum][0])
  self.radio_button1.config(text = answer_bank[qnum][1])
  self.radio_button2.config(text = answer_bank[qnum][2])
  self.radio_button3.config(text = answer_bank[qnum][3])
  self.radio_button4.config(text = answer_bank[qnum][4])

#function to randomise question order
def randomiser():
  global qnum
  qnum = random.randint(1, 8)
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