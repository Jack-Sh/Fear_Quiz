from tkinter import *
import csv
import random


class Quiz:

    def __init__(self):
        
        # common format for all buttons
        button_font = ("Arial", "10", "bold")

        # get all fears
        file = open("fear_list.csv", "r")
        all_fears = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        all_fears.pop(0)

        self.all_fear_list = []

        for item in range(0, 3):
            wrong_fears = random.choice(all_fears)

            self.all_fear_list.append(wrong_fears)

        correct_fear = random.choice(all_fears)

        self.all_fear_list.append(correct_fear)


        # Set up text frame
        self.text_frame = Frame(padx=10, pady=10)
        self.text_frame.grid()

        # Add question no# to frame
        self.question_label = Label(self.text_frame,
                                    text="Question 1/1",
                                    font=("Arial", "14", "bold"),
                                    anchor=W)

        self.question_label.grid(row=0, column=0, sticky=W)

        # Add fear placeholder to text frame
        self.fear_label = Label(self.text_frame,
                                text=correct_fear[0],
                                font=("Arial", "18", "bold"),
                                anchor=N)

        self.fear_label.grid(row=1, column=0, padx=10, pady=60, sticky=N)

        # create quiz frame (buttons)
        self.quiz_frame = Frame(self.text_frame)
        self.quiz_frame.grid(row=1, column=1)

        self.choice_buttons_ref = []

        # create 4 buttons (choice buttons)
        for item in range(0, 4):
            self.choice_buttons = Button(self.quiz_frame, bg="#80c5ff", font=button_font, width=12, height=2)

            self.choice_buttons_ref.append(self.choice_buttons)

            self.choice_buttons.grid(row=item // 2, column=item % 2, pady=15, padx=15)
        
        random.shuffle(self.all_fear_list)

        count = 0
        for item in self.choice_buttons_ref:
            item['text'] = self.all_fear_list[count][1]

            count += 1

        # adds a blank row to place 'next button' at bottom of window
        self.blank = Label(self.quiz_frame, text="")

        self.blank.grid(row=2, column=1, padx=10, pady=10)

        # add next button (for testing purposes this is hard coded)
        self.next_button = Button(self.quiz_frame, text="Next Question",
                            bg="#D5E8D4", font=button_font,  width=12)

        self.next_button.grid(row=3, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    Quiz()
    root.mainloop()