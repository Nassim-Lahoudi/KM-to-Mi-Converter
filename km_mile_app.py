import tkinter as tk
from tkinter import messagebox
from customtkinter import *


class Km_Mile_App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kilometer to Mile Converter")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.window.configure(bg="#F3F3F3")
        self.window.attributes("-topmost", True)

        set_appearance_mode("light")

        self.setup_widgets()

    def setup_widgets(self):
        self.label = tk.Label(self.window, text="Km to Mile Converter", font="Arial 12", bg="#F3F3F3")

        self.switch_mode = CTkSwitch(self.window, text="Light Dark \nMode", command=self.light_dark_mode_function)

        self.convert_entry = tk.Entry(self.window)
        self.submit_button = tk.Button(self.window, text="Convert", bg="#F3F3F3", borderwidth=0, command=self.submit_function)

        self.window.bind("<Return>", self.submit_function)

        self.label.pack(pady=5)
        self.convert_entry.pack(pady=15)
        self.submit_button.pack(pady=15)
        self.switch_mode.pack(pady=15)

    def light_dark_mode_function(self):
        value = self.switch_mode.get()
        if value:
            self.window.configure(bg="black")
            self.label.configure(bg="black", fg="#F3F3F3")
            self.submit_button.configure(bg="black", fg="#F3F3F3")
            set_appearance_mode("dark")
        else:
            self.window.configure(bg="#F3F3F3")
            self.label.configure(bg="#F3F3F3", fg="black")
            self.submit_button.configure(bg="#F3F3F3", fg="black")
            set_appearance_mode("light")

    def submit_function(self, event=None):
        user_input = self.convert_entry.get()
        if user_input:
            calculation = float(user_input) * float(0.621371)
            messagebox.showinfo("Result", f"The Result is {calculation}mi")
        else:
            messagebox.showerror("Error", "Please enter a Number")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Km_Mile_App()
    app.run()
