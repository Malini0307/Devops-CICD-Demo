import tkinter as tk
from registration import EmployeeRegistrationService

service = EmployeeRegistrationService()


def register():
    name = name_entry.get()
    email = email_entry.get()

    result = service.register_employee(name, email)

    message_label.config(text=result["message"])


root = tk.Tk()
root.title("Employee Registration")
root.geometry("400x300")

tk.Label(
    root,
    text="Employee Registration",
    font=("Arial", 16)
).pack(pady=10)

tk.Label(root, text="Employee Name").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email").pack()

email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Button(
    root,
    text="Register",
    command=register
).pack(pady=10)

message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()