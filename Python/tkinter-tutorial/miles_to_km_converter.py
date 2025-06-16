from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_resul_label.config(text=f"{km}")



miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

km_resul_label = Label(text=0)
km_resul_label.grid(row=1, column=1)

km_label = Label(text="Kilos")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()