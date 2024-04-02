from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from assign_manager import AssignmentManager
from teacher_notice import NoticeBoardManager
from teacher_payments import PaymentSystem
from teacher_student_attend import AttendanceManager


# import tkinter as tk
# from tkinter import messagebox


# class LoginSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Project - Login")
#         self.root.geometry("400x300")

#         self.label_title = tk.Label(root, text="Login System", font=("Helvetica", 20))
#         self.label_title.pack(pady=10)

#         self.label_username = tk.Label(root, text="Username:")
#         self.label_username.pack(pady=5)
#         self.entry_username = tk.Entry(root)
#         self.entry_username.pack()

#         self.label_password = tk.Label(root, text="Password:")
#         self.label_password.pack(pady=5)
#         self.entry_password = tk.Entry(root, show="*")
#         self.entry_password.pack()

#         self.btn_login = tk.Button(root, text="Login", command=self.login)
#         self.btn_login.pack(pady=10)

#     def login(self):
#         username = self.entry_username.get()
#         password = self.entry_password.get()

#         # Perform authentication (replace with your own logic)
#         if username == "student" and password == "student":
#             messagebox.showinfo("Login Successful", "Welcome, Student!")
#             self.root.destroy()  # Close login window
#             Dashboard("student")
#         elif username == "parent" and password == "parent":
#             messagebox.showinfo("Login Successful", "Welcome, Parent!")
#             self.root.destroy()  # Close login window
#             Dashboard("parent")
#         elif username == "teacher" and password == "teacher":
#             messagebox.showinfo("Login Successful", "Welcome, Teacher!")
#             self.root.destroy()  # Close login window
#             Dashboard("teacher")
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password")


# class Dashboard:
#     def __init__(self, user_type):
#         self.root = tk.Tk()
#         self.root.title("Student Project - Dashboard")
#         self.root.geometry("600x400")

#         self.user_type = user_type
#         self.setup_dashboard()

#     def setup_dashboard(self):
#         label_title = tk.Label(self.root, text=f"{self.user_type.capitalize()} Dashboard",
#                                font=("Helvetica", 20))
#         label_title.pack(pady=10)

#         if self.user_type == "student":
#             btn_view_grades = tk.Button(self.root, text="View Grades", command=self.view_grades)
#             btn_view_grades.pack(pady=5)
#             btn_view_attendance = tk.Button(self.root, text="View Attendance", command=self.view_attendance)
#             btn_view_attendance.pack(pady=5)
#         elif self.user_type == "parent":
#             btn_view_child_grades = tk.Button(self.root, text="View Child's Grades", command=self.view_child_grades)
#             btn_view_child_grades.pack(pady=5)
#             btn_view_child_attendance = tk.Button(self.root, text="View Child's Attendance",
#                                                   command=self.view_child_attendance)
#             btn_view_child_attendance.pack(pady=5)
#             btn_view_notices = tk.Button(self.root, text="View School Notices", command=self.view_notices)
#             btn_view_notices.pack(pady=5)
#         elif self.user_type == "teacher":
#             btn_manage_attendance = tk.Button(self.root, text="Manage Attendance", command=self.manage_attendance)
#             btn_manage_attendance.pack(pady=5)
#             btn_manage_assignments = tk.Button(self.root, text="Manage Assignments", command=self.manage_assignments)
#             btn_manage_assignments.pack(pady=5)
#             btn_manage_notices = tk.Button(self.root, text="Manage Notices", command=self.manage_notices)
#             btn_manage_notices.pack(pady=5)

#     def view_grades(self):
#         messagebox.showinfo("View Grades", "Viewing Grades...")

#     def view_attendance(self):
#         messagebox.showinfo("View Attendance", "Viewing Attendance...")

#     def view_child_grades(self):
#         messagebox.showinfo("View Child's Grades", "Viewing Child's Grades...")

#     def view_child_attendance(self):
#         messagebox.showinfo("View Child's Attendance", "Viewing Child's Attendance...")

#     def view_notices(self):
#         messagebox.showinfo("View Notices", "Viewing Notices...")

#     def manage_attendance(self):
#         messagebox.showinfo("Manage Attendance", "Managing Attendance...")

#     def manage_assignments(self):
#         messagebox.showinfo("Manage Assignments", "Managing Assignments...")

#     def manage_notices(self):
#         messagebox.showinfo("Manage Notices", "Managing Notices...")

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     root = tk.Tk()
#     login_system = LoginSystem(root)
#     root.mainloop()

#######################################################################################################################################

import tkinter as tk
from tkinter import messagebox

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Project - Login")
        self.root.geometry("400x300")

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

        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.pack(pady=10)

        self.btn_signup = tk.Button(root, text="Sign Up", command=self.open_signup_window)
        self.btn_signup.pack(pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Perform authentication (replace with your own logic)
        if username == "student" and password == "student":
            messagebox.showinfo("Login Successful", "Welcome, Student!")
            self.root.destroy()  # Close login window
            Dashboard("student")
        elif username == "parent" and password == "parent":
            messagebox.showinfo("Login Successful", "Welcome, Parent!")
            self.root.destroy()  # Close login window
            Dashboard("parent")
        elif username == "teacher" and password == "teacher":
            messagebox.showinfo("Login Successful", "Welcome, Teacher!")
            self.root.destroy()  # Close login window
            Dashboard("teacher")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("300x200")

        label_username = tk.Label(signup_window, text="Username:")
        label_username.pack(pady=5)
        entry_username = tk.Entry(signup_window)
        entry_username.pack()

        label_password = tk.Label(signup_window, text="Password:")
        label_password.pack(pady=5)
        entry_password = tk.Entry(signup_window, show="*")
        entry_password.pack()

        btn_register = tk.Button(signup_window, text="Register", command=lambda: self.register_user(entry_username.get(), entry_password.get()))
        btn_register.pack(pady=10)

    def register_user(self, username, password):
        # Here you can implement your registration logic
        # For demonstration purposes, just show a message box
        messagebox.showinfo("Registration", f"Registered User: {username}")

class Dashboard:
    def __init__(self, user_type):
        self.root = tk.Tk()
        self.root.title("Student Project - Dashboard")
        self.root.geometry("600x400")

        self.user_type = user_type
        self.setup_dashboard()

    def setup_dashboard(self):
        label_title = tk.Label(self.root, text=f"{self.user_type.capitalize()} Dashboard",
                               font=("Helvetica", 20))
        label_title.pack(pady=10)

        # Add dashboard components based on user type

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    login_system = LoginSystem(root)
    root.mainloop()