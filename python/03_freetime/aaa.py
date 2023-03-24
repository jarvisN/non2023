import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os
import math


class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")

        # Initialize list to store input values
        self.input_history = []

        self.label1 = tk.Label(master, text="Input 1:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Input 2:")
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)

        self.label3 = tk.Label(master, text="Input 3:")
        self.label3.grid(row=2, column=0)
        self.entry3 = tk.Entry(master)
        self.entry3.grid(row=2, column=1)
        self.submit_button = tk.Button(master, text="Submit", command=lambda: [
                                       self.check_data(), self.submit(), self.clear_entry()])
        self.submit_button.grid(row=4, column=0)

        self.result_label = tk.Label(master, text=" ")
        self.result_label.grid(row=3, column=0, columnspan=2)

        # Table to display input data
        self.treeview = ttk.Treeview(master, columns=(
            'Datetime', 'Input 1', 'Input 2', 'Input 3', 'Result'), displaycolumns=(0, 1, 2, 3, 4))
        self.treeview.grid(row=7, column=0, columnspan=2)
        self.treeview.column('#0', width=0, stretch="no")
        self.treeview.heading('Datetime', text='Datetime')
        self.treeview.heading('Input 1', text='Input 1')
        self.treeview.heading('Input 2', text='Input 2')
        self.treeview.heading('Input 3', text='Input 3')
        self.treeview.heading('Result', text='Result')

        # Save csv
        self.label4 = tk.Label(master, text="File Name : ")
        self.label4.grid(row=4, column=1)  # Changed from (4,0) to (4,1)
        self.entry4 = tk.Entry(master)
        self.entry4.grid(row=4, column=2)

        # self.save_button = tk.Button(master, text="Save", command=self.save_data)
        self.save_button = tk.Button(
            master, text="Save", command=self.save_data)

        self.save_button.grid(row=4, column=3)

        # exit

        self.close_button = tk.Button(
            master, text="Close", command=master.destroy)
        self.close_button.grid(row=8, column=0, columnspan=2)
        
        
        self.graph_button = tk.Button(master, text="Show Graph", command=self.show_graph)
        self.graph_button.grid(row=5, column=0)
        
        self.clear_button = tk.Button(master, text="Clear Input History", command=self.clear_input_history)
        self.clear_button.grid(row=6, column=0, columnspan=2)

    def clear_input_history(self):
        
        self.input_history.clear()
        messagebox.showinfo("Info", "Input history has been cleared.")

    def clear_entry(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

    def check_data(self):
        input1 = self.entry1.get().strip()
        input2 = self.entry2.get().strip()
        input3 = self.entry3.get().strip()

        if not input1:
            messagebox.showerror("Error", "Input 1 is empty")
            return

        if not input2:
            messagebox.showerror("Error", "Input 2 is empty")
            return

        if not input3:
            messagebox.showerror("Error", "Input 3 is empty")
            return

        return True

    def submit(self):

        input1 = self.entry1.get().strip()
        input2 = self.entry2.get().strip()
        input3 = self.entry3.get().strip()

        data1 = int(input1)
        data2 = int(input2)
        data3 = int(input3)

        result = self.calculate(data1, data2, data3)
        self.result_label.configure(text=f"Result: {result}")

        # Get current timestamp
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if data3 == 1:
            data3 = 'Add'
        elif data3 == 2:
            data3 = 'Subtraction'
        elif data3 == 3:
            data3 = 'Multiply'
        elif data3 == 4:
            data3 = 'Divide'
        else:
            data3 = "error : value is not define"
            return

        self.treeview.insert('', 'end', values=(
            timestamp, data1, data2, data3, result))

    def calculate(self, data1, data2, data3):
        if data3 == 1:
            return data1 + data2
        elif data3 == 2:
            return data1 - data2
        elif data3 == 3:
            return data1 * data2
        elif data3 == 4:
            return data1 / data2
        else:
            return "error : Nothing"
        
    def show_graph(self):
        # Get the data from the treeview
        data = []
        for child in self.treeview.get_children():
            values = self.treeview.item(child)['values']
            data.append(values[4])  # Append the result to the data list
        
        # Create a simple bar graph of the results
        
        # print(data)
        # print(len(data))
        
        plt.bar(range(int(len(data))), data)
        plt.title("Results")
        plt.xlabel("Input")
        plt.ylabel("Result")
        plt.show()

    def save_data(self):

        input4 = self.entry4.get().strip()

        print(len(input4))

        if len(input4) < 1:
            messagebox.showerror(
                "Error", "Please fill in your file name in the block space.")
            return
        else:

            file_path = self.entry4.get().strip()

            file_path = file_path + ".csv"

            # Get the data from the treeview
            data = []

            for child in self.treeview.get_children():
                values = self.treeview.item(child)['values']
                data.append(values)

            # print(data)
            # print(values)
            # print(len(data))

            if len(data) < 1:
                messagebox.showerror(
                    "Error", "Cannot save CSV file: input field is empty")
                return

            # Create a pandas dataframe with the data
            columns = ['Datetime', 'Input 1', 'Input 2', 'Input 3', 'Result']
            new_data = pd.DataFrame(data, columns=columns)

            # print(new_data)

            if os.path.exists(file_path):
                # file exists, append new data to it
                existing_data = pd.read_csv(file_path)
                all_data = pd.concat([existing_data, new_data])
                all_data.to_csv(file_path, index=False)
                messagebox.showinfo(
                    "Save", f'Saved, Data saved to {file_path}')

            else:
                # file doesn't exist, create new file with new data
                new_data.to_csv(file_path, index=False)
                messagebox.showinfo(
                    "Save", f'Saved , New File Data saved to {file_path}')
                
        


root = tk.Tk()
my_gui = MyGUI(root)
# root.geometry("1200x370")
root.attributes('-fullscreen', True)

entry = tk.Entry(root)
root.mainloop()
