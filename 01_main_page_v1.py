from tkinter import *


class MainPage:

    def __init__(self):
        
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

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

        # Add entry form to frame and an error message beneath it
        self.question_frame = Frame(self.main_frame)
        self.question_frame.grid(row=2)

        self.main_entry = Entry(self.question_frame,
                                font=("Arial", "14"))

        self.main_entry.grid(row=0, column=0, padx=10, pady=10)

        self.go_button = Button(self.question_frame, text="Go",
                                bg="#D5E8D4", fg="#000000",
                                font=button_font, width=6)

        self.go_button.grid(row=0, column=1)

        error = "Please enter a whole number between 1 and 50"

        self.output_label = Label(self.main_frame, text=error,
                                fg="#9C0000")
        self.output_label.grid(row=3)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    MainPage()
    root.mainloop()