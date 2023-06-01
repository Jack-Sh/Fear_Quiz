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

        self.question_label = Label(self.text_frame,
                                  text="Question 1/1",
                                  font=("Arial", "18", "bold"))

        self.question_label.grid(row=0, column=0)

        self.fear_label = Label(self.text_frame,
                                text="Fear Goes Here...",
                                font=("Arial", "14", "bold"))

        self.fear_label.grid(row=1, column=0, padx=10)

        self.quiz_frame = Frame(self.text_frame)
        self.quiz_frame.grid(row=1, column=1, pady=20)

        self.button_1 = Button(self.quiz_frame, text="Button 1",
                        bg="#D5E8D4", font=button_font, width=12, height=2)

        self.button_1.grid(row=0, column=0, pady=15, padx=15)

        self.button_2 = Button(self.quiz_frame, text="Button 2",
                        bg="#D5E8D4", font=button_font, width=12, height=2)

        self.button_2.grid(row=0, column=1, pady=15, padx=15)

        self.button_3 = Button(self.quiz_frame, text="Button 3",
                        bg="#D5E8D4", font=button_font, width=12, height=2)

        self.button_3.grid(row=1, column=0, pady=15, padx=15)

        self.button_4 = Button(self.quiz_frame, text="Button 4",
                        bg="#D5E8D4", font=button_font, width=12, height=2)

        self.button_4.grid(row=1, column=1, pady=15, padx=15)

        self.next_button = Button(self.quiz_frame, text="Next Question",
                        bg="#D5E8D4", font=button_font)

        self.next_button.grid(row=2, column=1, pady=20)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    Quiz()
    root.mainloop()