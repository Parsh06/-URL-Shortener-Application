from tkinter import *
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners
import validators
import pyperclip

class UrlShortener:
    def create(self):
        url = self.url_entry.get()
        if not validators.url(url):
            messagebox.showerror("Error", "Please enter a valid URL")
        else:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            self.output_entry.delete(0, END)
            self.output_entry.insert(END, short_url)

    def copy_to_clipboard(self):
        short_url = self.output_entry.get()
        if short_url:
            pyperclip.copy(short_url)
            messagebox.showinfo("Success", "Short URL copied to clipboard")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x200')
        self.root.maxsize(500, 200)
        self.root.minsize(500, 200)
        self.root.title('URL Shortener')
        self.root['bg'] = "black"  # Change background color to black

        title_label = Label(self.root, text="URL Shortener", font=('times', 15, 'bold'), bg="black", fg="red")  # Change font to roman, text color to red
        title_label.place(x=180, y=5)

        date_label = Label(self.root, text=datetime.now().date(), fg="red", font=('times', 10, 'bold'), bg="black")  # Change font to roman, text color to red
        date_label.place(x=400, y=5)

        url_label = Label(self.root, text="Paste Your URL Here ..", font=('times', 10, 'bold'), fg="red", bg="black")  # Change font to roman, text color to red
        url_label.place(x=50, y=50)

        self.url_entry = Entry(self.root, width=50, bg="pink", relief=GROOVE, borderwidth=2, border=2)  # Change input fields background color to pink
        self.url_entry.place(x=50, y=80)
        self.url_entry.config(fg="red")  # Change text color of input fields to red
        self.url_entry.config(highlightbackground="yellow", highlightcolor="yellow", highlightthickness=2)  # Change border color to yellow

        create_button = Button(self.root, relief=GROOVE, text="Create", font=('times', 8, 'bold'), bg="red", fg="black", command=self.create)  # Change font to roman, button color to red, text color to black
        create_button.place(x=360, y=78)

        copy_button = Button(self.root, relief=GROOVE, text="Copy", font=('times', 8, 'bold'), bg="red", fg="black", command=self.copy_to_clipboard)  # Change font to roman, button color to red, text color to black
        copy_button.place(x=440, y=78)

        self.output_entry = Entry(self.root, font=('times', 10, 'bold'), fg="red", width=30, relief=GROOVE, borderwidth=2, border=2)  # Change font to roman, text color to red
        self.output_entry.place(x=80, y=120)
        self.output_entry.config(bg="pink")  # Change background color of output field to pink
        self.output_entry.config(highlightbackground="yellow", highlightcolor="yellow", highlightthickness=2)  # Change border color to yellow

        self.root.mainloop()


if __name__ == '__main__':
    UrlShortener()
