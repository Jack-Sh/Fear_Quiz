from tkinter import *


class Quiz:

    def __init__(self):
        
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "10", "bold")
        button_fg = "#FFFFFF"
        
        # Set up GUI Frame
        self.text_frame = Frame(padx=10, pady=10)
        self.text_frame.grid()

        # Add 'Fear Quiz' heading to frame
        self.question_label = Label(self.text_frame,
                                    text="Question 1/1",
                                    font=("Arial", "14", "bold"),
                                    anchor=W)

        self.question_label.grid(row=0, column=0, sticky=W)

        self.fear_label = Label(self.text_frame,
                                text="Fear Goes Here...",
                                font=("Arial", "18", "bold"),
                                anchor=N)

        self.fear_label.grid(row=1, column=0, padx=10, pady=60, sticky=N)

        # Add entry form to frame and an error message beneath it
        self.quiz_frame = Frame(self.text_frame)
        self.quiz_frame.grid(row=1, column=1)

        for item in range(0,4):
            self.choice_buttons = Button(self.quiz_frame, text="Button",
                            bg="#D5E8D4", font=button_font, width=12, height=2)

            self.choice_buttons.grid(row=item // 2, column=item % 2, pady=15, padx=15)

        self.next_button = Button(self.quiz_frame, text="Next Question",
                            bg="#D5E8D4", font=button_font, width=12)

        self.next_button.grid(row=2, column=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    Quiz()
    root.mainloop()