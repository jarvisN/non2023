import tkinter as tk

def validate_entry_number(*args):
    value = entry_number.get()
    if not value.isdigit():
        entry_number.delete(0, tk.END)  # clear the entry widget
    else:
        # do something with the input value
        print("Input value:", value)

root = tk.Tk()

entry_number = tk.Entry(root)
entry_number.pack()

# bind the function to the <KeyRelease> event of the entry widget
entry_number.bind('<KeyRelease>', validate_entry_number)

root.mainloop()
