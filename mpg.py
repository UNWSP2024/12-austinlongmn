# Programmer: Austin Long
# Date: 2025-04-22
# Program: MPG Calculator

import tkinter
import tkinter.messagebox


# creates a grided text field
def generate_text_field(label: str, frame, row):
    gui_label = tkinter.Label(frame, text=label)
    gui_label.grid(row=row, column=0, pady=2, sticky=tkinter.W)
    entry = tkinter.Entry(frame)
    entry.grid(row=row, column=1, pady=2)
    frame.pack()
    return entry


class MPGCalculator:
    def __init__(self) -> None:
        # create window
        self.main_window = tkinter.Tk()

        self.input_frame = tkinter.Frame()

        self.units_label = tkinter.Label(self.input_frame, text="All units are in gallons and miles.")
        self.units_label.grid(row=0, columnspan=2)
        # create entry for gallons
        self.hold_gallons_entry = generate_text_field(
            "Enter your tank's capacity:", self.input_frame, 1
        )

        # create entry for miles
        self.num_miles_entry = generate_text_field(
            "Number of miles on a full tank:", self.input_frame, 2
        )

        # create content frame
        self.button_frame = tkinter.Frame()

        # create button
        self.submit_button = tkinter.Button(
            self.button_frame, text="Submit", command=self.show_info
        )
        self.submit_button.pack(side="left")

        # create quit button
        self.quit_button = tkinter.Button(
            self.button_frame, text="Quit", command=self.main_window.quit
        )
        self.quit_button.pack(side="left")

        self.input_frame.pack(pady=20)
        self.button_frame.pack(pady=10)

        # set window title
        self.main_window.title("MPG Calculator")

        # set minimum window size
        self.main_window.minsize(16 * 30, 9 * 30)

        # run program
        tkinter.mainloop()

    def show_info(self):
        try:
            num_miles = float(self.num_miles_entry.get())
            gallons = float(self.hold_gallons_entry.get())

            mpg = num_miles / gallons

            tkinter.messagebox.showinfo(title="MPG", message=f"You will get {mpg:.2f} MPG")
        except ValueError:
            tkinter.messagebox.showerror(
                title="Invalid input",
                message="One or more input boxes was not a number.",
            )


if __name__ == "__main__":
    program = MPGCalculator()
