import requests
import csv
import tkinter as tk

def read_csv(file_name):
    emails = []
    with open("MOCK_DATA.csv", "r", newline='') as file:
        has_header = next(file, None)
        file.seek(0)
        email_data = csv.reader(file, delimiter=",")
        if has_header:
            next(email_data)
        for row in email_data:
            email = {"email": row[2]}
            print(email)
            emails.append(email)
    submit_emails(emails)
    
def submit_emails(emails):
    for email in emails:
        payload = email
        print(payload)
        r = requests.post("https://chapelhillpubliclibrary.org/library-newsletters/", data=payload)
        print(r)


class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Batch Email Submittal")
        self.label = tk.Label(self.root, text= "Enter the CSV file name")
        self.label.pack()


        self.entrytext = tk.StringVar()
        tk.Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = tk.StringVar()
        self.buttontext.set("Submit")
        tk.Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = tk.Label(self.root, text="")
        self.label.pack()

        self.root.mainloop()

    def clicked1(self):
        input = self.entrytext.get()
        file_name = str(input) + ".csv"
        self.label.configure(text=file_name)
        read_csv(file_name)

    def button_click(self, e, file_name):
        read_csv(file_name)
        
App()
