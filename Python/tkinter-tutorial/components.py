import tkinter as tk

def button_clicked():
    label_text = f"Entry: {entry.get()}, Radio: {radio_var.get()}, Scale: {scale.get()}, Checkbox: {check_var.get()}"
    my_label.config(text=label_text)
    print("Text Area Content:", text_area.get("1.0", tk.END))

def listbox_selected(event):
    selected_item = listbox.get(listbox.curselection())
    my_label.config(text=f"Listbox selected: {selected_item}")

window = tk.Tk()
window.title("My first GUI")
window.minsize(width=600, height=600)

# Label
my_label = tk.Label(text="Hello, World!", font=("Arial", 20, "bold"))
my_label.pack(pady=10)

# Entry
entry = tk.Entry(width=30)
entry.pack()

# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.pack(pady=5)

# Radio Buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(text="Option 1", value="Option 1", variable=radio_var)
radio2 = tk.Radiobutton(text="Option 2", value="Option 2", variable=radio_var)
radio1.pack()
radio2.pack()

# Scale
scale = tk.Scale(from_=0, to=100, orient="horizontal", label="Volume")
scale.pack()

# Checkbox
check_var = tk.BooleanVar()
check_button = tk.Checkbutton(text="I agree", variable=check_var)
check_button.pack()

# Text Area
text_area = tk.Text(height=5, width=40)
text_area.insert(tk.END, "Write something here...")
text_area.pack()

# Listbox
listbox = tk.Listbox(height=4)
items = ["Apple", "Banana", "Cherry", "Date"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack()
listbox.bind("<<ListboxSelect>>", listbox_selected)

window.mainloop()




# https://docs.python.org/3/library/tkinter.html#the-packer