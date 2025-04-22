# Programmer: Austin Long
# Date: 2025-04-22
# Program: Long-Distance Calls

import tkinter
import tkinter.messagebox

RATE_DAYTIME = 0.02
RATE_EVENING = 0.12
RATE_OFF_PEAK = 0.05

class CallCalculator:
    def __init__(self) -> None:
        # create window
        self.main_window = tkinter.Tk()

        self.input_frame = tkinter.Frame()

        self.selected_time_var = tkinter.IntVar()
        self.selected_time_var.set(0)

        tkinter.Radiobutton(self.input_frame, text=f"Daytime (6:00 A.M. through 5:59 P.M.): ${RATE_DAYTIME:.2f}", value=0, variable=self.selected_time_var).pack()
        tkinter.Radiobutton(self.input_frame, text=f"Evening (6:00 P.M. through 11:59 P.M.): ${RATE_EVENING:.2f}", value=1, variable=self.selected_time_var).pack()
        tkinter.Radiobutton(self.input_frame, text=f"Off-Peak (midnight through 5:59 P.M.): ${RATE_OFF_PEAK:.2f}", value=2, variable=self.selected_time_var).pack()

        gui_label = tkinter.Label(self.input_frame, text="Number of minutes on call:")
        gui_label.pack(side="left")
        self.minutes_entry = tkinter.Entry(self.input_frame)
        self.minutes_entry.pack(side="left")

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
        self.main_window.title("Long-Distance Call Calculator")

        # set minimum window size
        self.main_window.minsize(16 * 30, 9 * 30)

        # run program
        tkinter.mainloop()

    def show_info(self):
        try:
            rate = -1
            selected_item = self.selected_time_var.get()

            if selected_item == 0:
                rate = RATE_DAYTIME
            elif selected_item == 1:
                rate = RATE_EVENING
            elif selected_item == 2:
                rate = RATE_OFF_PEAK
            else:
                raise RuntimeError("selected_item must be 0, 1, or 2.")

            minutes = float(self.minutes_entry.get())

            tkinter.messagebox.showinfo(title="Cost", message=f"This will cost you ${minutes * rate:.2f}")
        except ValueError:
            tkinter.messagebox.showerror(
                title="Invalid input",
                message="One or more input boxes was not a number.",
            )


if __name__ == "__main__":
    program = CallCalculator()
