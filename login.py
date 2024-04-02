import tkinter as tk
from tkinter import messagebox

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")

        # Create labels
        self.label_title = tk.Label(root, text="Login System", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        # Create buttons
        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.pack(pady=10)

        self.btn_register = tk.Button(root, text="Register", command=self.register)
        self.btn_register.pack(pady=5)

        self.btn_forgot_password = tk.Button(root, text="Forgot Password", command=self.forgot_password)
        self.btn_forgot_password.pack(pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simulate authentication
        if username == "student" and password == "student":
            messagebox.showinfo("Login Successful", "Welcome, Student!")
        elif username == "parent" and password == "parent":
            messagebox.showinfo("Login Successful", "Welcome, Parent!")
        elif username == "teacher" and password == "teacher":
            self.open_administration()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_administration(self):
        # Close login window
        self.root.destroy()

        # Open administration window
        admin_window = tk.Tk()
        admin_window.title("Administration")
        admin_window.geometry("400x300")

        # Create labels
        label_admin = tk.Label(admin_window, text="Welcome, Teacher!", font=("Helvetica", 20))
        label_admin.pack(pady=10)

        # Create buttons for administration tasks
        btn_fees = tk.Button(admin_window, text="View Fees", command=self.view_fees)
        btn_fees.pack(pady=5)

        btn_attendance = tk.Button(admin_window, text="View Attendance", command=self.view_attendance)
        btn_attendance.pack(pady=5)

        btn_marks = tk.Button(admin_window, text="View Marks", command=self.view_marks)
        btn_marks.pack(pady=5)

        btn_upload_assignment = tk.Button(admin_window, text="Upload Assignment", command=self.upload_assignment)
        btn_upload_assignment.pack(pady=5)

        btn_upload_advertisement = tk.Button(admin_window, text="Upload Advertisement", command=self.upload_advertisement)
        btn_upload_advertisement.pack(pady=5)

        # Run administration window
        admin_window.mainloop()

    def view_fees(self):
        messagebox.showinfo("View Fees", "Functionality to view fees will be implemented here")

    def view_attendance(self):
        messagebox.showinfo("View Attendance", "Functionality to view attendance will be implemented here")

    def view_marks(self):
        messagebox.showinfo("View Marks", "Functionality to view marks will be implemented here")

    def upload_assignment(self):
        messagebox.showinfo("Upload Assignment", "Functionality to upload assignment will be implemented here")

    def upload_advertisement(self):
        messagebox.showinfo("Upload Advertisement", "Functionality to upload advertisement will be implemented here")

    def register(self):
        messagebox.showinfo("Register", "Functionality for registration will be implemented here")

    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "Functionality for password recovery will be implemented here")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()