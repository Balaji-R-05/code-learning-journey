import tkinter as tk

def button_clicked():
    print("Button got clicked!")
    input_text = input.get()
    my_label.config(text=input_text)


window = tk.Tk()
window.title("My first GUI")
window.minsize(width=500, height=400)

# Label
my_label = tk.Label(text="Hello, World!", font=("Arial", 24, "bold"))
my_label.pack()
# my_label["text"] = "Welcome"
# my_label.config(text="Welcome")

# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.pack()


input = tk.Entry(width=30)
input.pack()

window.mainloop()



# https://docs.python.org/3/library/tkinter.html#the-packer