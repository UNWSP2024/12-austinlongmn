# Programmer: Austin Long
# Date: 2025-04-22
# Program: Joe's Automotive

import tkinter
import tkinter.messagebox

JOB_TYPES = [
    {"type": "Oil Change", "price": 30.0},
    {"type": "Lube Job", "price": 20.0},
    {"type": "Radiator Flush", "price": 40.00},
    {"type": "Transmission Fluid", "price": 100.00},
    {"type": "Inspection", "price": 35.00},
    {"type": "Muffler replacement", "price": 200.00},
    {"type": "Tire Rotation", "price": 20.00},
]


class JoesAutomotive:
    def __init__(self) -> None:
        # create window
        self.main_window = tkinter.Tk()

        self.input_frame = tkinter.Frame()

        # create a check box for each job type
        self.type_vars = []
        for i in range(len(JOB_TYPES)):
            is_on_var = tkinter.IntVar()
            is_on_var.set(0)
            tkinter.Checkbutton(
                self.input_frame,
                text=f"{JOB_TYPES[i]['type']} - ${JOB_TYPES[i]['price']:.2f}",
                variable=is_on_var,
                command=self.update_price,
            ).pack()
            self.type_vars.append(is_on_var)

        # create content frame
        self.button_frame = tkinter.Frame()

        self.result_frame = tkinter.Frame()

        # create label for result
        self.total_charges_text = tkinter.StringVar()
        self.total_charges_label = tkinter.Label(
            self.result_frame, textvariable=self.total_charges_text
        )
        self.total_charges_label.pack()

        self.update_price()

        self.clear_button = tkinter.Button(
            self.button_frame, text="Clear", command=self.clear
        )
        self.clear_button.pack(side="left")

        self.select_all_button = tkinter.Button(
            self.button_frame, text="Select All", command=self.select_all
        )
        self.select_all_button.pack(side="left")

        # create quit button
        self.quit_button = tkinter.Button(
            self.button_frame, text="Quit", command=self.main_window.quit
        )
        self.quit_button.pack(side="left")

        self.input_frame.pack(pady=20)
        self.result_frame.pack()
        self.button_frame.pack(pady=10)

        # set window title
        self.main_window.title("Joe's Automotive")

        # set minimum window size
        self.main_window.minsize(16 * 30, 9 * 30)

        # run program
        tkinter.mainloop()

    def select_all(self):
        for var in self.type_vars:
            var.set(1)
        self.update_price()

    def clear(self):
        for var in self.type_vars:
            var.set(0)
        self.update_price()

    def update_price(self):
        checks = list(map(lambda x: x.get(), self.type_vars))

        result = 0.0
        for i in range(len(checks)):
            if checks[i]:
                result += JOB_TYPES[i]["price"]

        self.total_charges_text.set(f"Your total price: ${result:.2f}")


if __name__ == "__main__":
    program = JoesAutomotive()
