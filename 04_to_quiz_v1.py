from tkinter import *
from functools import partial


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
        continues = "Valid response"

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
                                text="Fear Goes Here...",
                                font=("Arial", "18", "bold"),
                                anchor=N)

        self.fear_label.grid(row=1, column=0, padx=10, pady=60, sticky=N)

        # create quiz frame (buttons)
        self.quiz_frame = Frame(self.text_frame)
        self.quiz_frame.grid(row=1, column=1)

        # create 4 buttons (choice buttons)
        for item in range(0, 4):
            self.choice_buttons = Button(self.quiz_frame, text="Button",
                            bg="#80c5ff", font=button_font, width=12, height=2)

            self.choice_buttons.grid(row=item // 2, column=item % 2, pady=15, padx=15)
        
        # adds a blank row to place 'next button' at bottom of window
        self.blank = Label(self.quiz_frame, text="")

        self.blank.grid(row=2, column=1, padx=10, pady=10)

        # add next button (for testing purposes this is hard coded)
        self.next_button = Button(self.quiz_frame, text="Next Question",
                            bg="#D5E8D4", font=button_font, width=12)

        self.next_button.grid(row=3, column=1)


    def close_quiz(self):

        root.deiconify()
        self.quiz_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    MainPage()
    root.mainloop()