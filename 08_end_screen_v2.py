from tkinter import *
from functools import partial
import csv
import random


class MainPage:

    def __init__(self):
        
        
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "10", "bold")
        
        # Set up GUI Frame
        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        # Add 'Fear Quiz' heading to frame
        self.main_heading = Label(self.main_frame,
                                  text="Fear Quiz",
                                  font=("Arial", "24", "bold"))

        self.main_heading.grid(row=0, pady=20)

        # Add sub-heading question to frame
        self.main_subheading = Label(self.main_frame,
                                    text="How Many Questions?",
                                    font=("Arial", "14", "bold"))
    
        self.main_subheading.grid(row=1)

        # Add entry form to frame and a go button next to it
        self.question_frame = Frame(self.main_frame)
        self.question_frame.grid(row=2)

        self.main_entry = Entry(self.question_frame,
                                font=("Arial", "14"))

        self.main_entry.grid(row=0, column=0, padx=10, pady=10)

        self.go_button = Button(self.question_frame, text="Go",
                                bg="#D5E8D4", font=button_font, width=5,
                                command=lambda: self.check_questions())

        self.go_button.grid(row=0, column=1)

        # Add the output label (error message) below the entry form
        self.output_label = Label(self.main_frame, text="")
        self.output_label.grid(row=3)


    # checks user input and if it's valid
    def check_questions(self):
        
        # setup variables for future flexability
        has_error = "no"
        error = "Please enter a whole number between 1 and 50"

        # get response and check that it is between max and min
        response = self.main_entry.get()

        try:
            response = int(response)

            if response > 0 and response < 51:
                has_error = "no"

            else:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # prints error message if its an invalid input
        if has_error == "yes":
            self.output_label.config(text=error, fg="#9C0000")
            self.main_entry.config(bg="#F8CECC")
        
        # if we have no errors
        else:
            self.to_quiz(response)


    def to_quiz(self, num_questions):
        Quiz(num_questions)

        root.withdraw()


class Quiz:

    def __init__(self, how_many):

        # Variables used to work out statistics, when game ends etc
        self.questions_wanted = IntVar()
        self.questions_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.questions_answered = IntVar()
        self.questions_answered.set(0)

        self.question_fear_list = []

        self.correct_answers = 0
        self.incorrect_answers = 0

        self.quiz_box = Toplevel()

        self.quiz_box.protocol('WM_DELETE_WINDOW', partial(self.close_quiz))
        
        # common format for all buttons
        button_font = ("Arial", "10", "bold")
        
        # Set up text frame
        self.text_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.text_frame.grid()

        question_heading = "Question 1 of {}".format(how_many)

        # Add question no# to frame
        self.question_label = Label(self.text_frame,
                                    text=question_heading,
                                    font=("Arial", "14", "bold"),
                                    anchor=W)

        self.question_label.grid(row=0, column=0, sticky=W)

        # Add fear placeholder to text frame
        self.fear_label = Label(self.text_frame,
                                text="",
                                font=("Arial", "18", "bold"),
                                anchor=N)

        self.fear_label.grid(row=1, column=0, padx=10, pady=60, sticky=N)

        # create quiz frame (buttons)
        self.quiz_frame = Frame(self.text_frame)
        self.quiz_frame.grid(row=1, column=1)

        self.choice_buttons_ref = []
        self.button_fear_list = []

        # create 4 buttons (choice buttons)
        for item in range(0, 4):
            self.choice_buttons = Button(self.quiz_frame, bg="#80c5ff", font=button_font, width=12, height=2, command=lambda i=item: self.check_answer(self.button_fear_list[i]))

            self.choice_buttons_ref.append(self.choice_buttons)

            self.choice_buttons.grid(row=item // 2, column=item % 2, pady=15, padx=15)

        # adds a blank row to place 'next button' at bottom of window
        self.blank = Label(self.quiz_frame, text="")

        self.blank.grid(row=2, column=1, padx=10, pady=10)

        # add next button
        self.next_button = Button(self.quiz_frame, text="Next Question",
                            bg="#D5E8D4", font=button_font, width=12, command=self.new_question)

        self.next_button.grid(row=3, column=1)

        self.new_question()


    def get_fears(self):

        # get all fears
        file = open("fear_list.csv", "r")
        all_fears = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        all_fears.pop(0)

        # create a list of fears for a question
        self.question_fear_list = []

        # get 4 random fears answers
        while len(self.question_fear_list) < 4:

            fears = random.choice(all_fears)

            self.question_fear_list.append(fears)

        return self.question_fear_list


    def new_question(self):

        # get the current question no# and total question no#
        how_many = self.questions_wanted.get()
        current_question = self.questions_answered.get()

        # add 1 to the question counter
        current_question += 1
        self.questions_answered.set(current_question)

        # update the question heading
        new_heading = "Question {} of {}".format(current_question, how_many)
        self.question_label.config(text=new_heading)
        
        # disable next button until the question is answered
        self.next_button.config(state=DISABLED)

        # get the fears for the question
        self.button_fear_list = self.get_fears()

        # generate a random number to associate with the correct fear
        self.button_number = random.randint(0, 3)

        # get correct fear from the list
        self.correct_fear = self.button_fear_list[self.button_number]

        # display the 'correct' fear
        self.fear_label.config(text=self.correct_fear[0])
        
        # *** For testing ***
        print(self.button_fear_list)

        # place the shuffled fears in the choice buttons
        count = 0
        for item in self.choice_buttons_ref:
            item['text'] = self.button_fear_list[count][1]
            item['bg'] = "#80c5ff"
            item['state'] = NORMAL

            count += 1
        
        # return the asnwer
        return self.correct_fear


    # function to check the users answer
    def check_answer(self, user_answer):
        
        # get current question and the total number of questions
        how_many = self.questions_wanted.get()
        current_question = self.questions_answered.get()

        # grab the correct fear
        correct_answer = self.correct_fear

        # if the user gets the correct answer, add one to the counter
        if user_answer[1] == correct_answer[1]:
            self.correct_answers += 1

        # if user selects incorrect answer, add one to the incorrect counter
        else:
            self.incorrect_answers += 1

        # disable the buttons and set the colour of all the buttons to red
        for item in self.choice_buttons_ref:
            item['state'] = DISABLED
            item['bg'] = "#ffcccb"

        # set the correct answer to green
        self.choice_buttons_ref[self.button_number].config(bg="#90EE90")

        # enable next button
        self.next_button.config(state=NORMAL)

        # if on last round, upon button press, enable the next button
        # change the text to end quiz and once pressed send user to end screen
        if how_many == current_question:
            self.next_button.config(text="End Quiz", command=lambda: self.to_end_screen())


    # if "end quiz" is pressed send user to end screen
    def to_end_screen(self):
        
        how_many = self.questions_wanted.get()

        EndScreen(how_many, self.correct_answers)
        self.quiz_box.destroy()


    # if the "X" is pressed close the quiz box and re-open the main page
    def close_quiz(self):

        root.deiconify()
        self.quiz_box.destroy()


class EndScreen:

    def __init__(self, how_many, correct_answers):
        
        # create end screen frame
        self.end_box = Toplevel()

        self.text_frame = Frame(self.end_box, padx=100, pady=10)
        self.text_frame.grid()
        
        # create labels, including the title and score
        self.title_label = Label(self.text_frame, text="Fear Quiz", font=("Arial", "20", "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.blank_line_1 = Label(self.text_frame, text="")
        self.blank_line_1.grid(row=1, column=0, pady=10)

        # format the score with correct answers and the number of questions answered
        score_readout = "You Got\n\n{} Out of {}\n\nCorrect!".format(correct_answers, how_many)

        self.score_text = Label(self.text_frame, text=score_readout, font=("Arial", "16", "bold"))
        self.score_text.grid(row=2, column=0, padx=5, pady=5)

        self.blank_line_2 = Label(self.text_frame, text="")
        self.blank_line_2.grid(row=3, column=0, pady=10)

        # create a restart quiz button. upon press, sends user to the main page
        self.restart_button = Button(self.text_frame, text="Restart Quiz", font=("Arial", "10", "bold"), width=12, height=2, bg="#D5E8D4", command=lambda: self.restart_quiz())
        self.restart_button.grid(row=4, column=0, padx=10, pady=10)

    
    # sends user to mainpage upon restart button press
    def restart_quiz(self):
        
        root.deiconify()
        self.end_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    MainPage()
    root.mainloop()