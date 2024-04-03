from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from assign_manager import AssignmentManager
from teacher_notice import NoticeBoardManager
from teacher_payments import PaymentSystem
from teacher_student_attend import AttendanceManager

import tkinter as tk
from tkinter import messagebox
#################################################################################################################################################################
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

#         self.btn_signup = tk.Button(root, text="Sign Up", command=self.open_signup_window)
#         self.btn_signup.pack(pady=5)

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

#     def open_signup_window(self):
#         signup_window = tk.Toplevel(self.root)
#         signup_window.title("Sign Up")
#         signup_window.geometry("300x200")

#         label_username = tk.Label(signup_window, text="Username:")
#         label_username.pack(pady=5)
#         entry_username = tk.Entry(signup_window)
#         entry_username.pack()

#         label_password = tk.Label(signup_window, text="Password:")
#         label_password.pack(pady=5)
#         entry_password = tk.Entry(signup_window, show="*")
#         entry_password.pack()

#         btn_register = tk.Button(signup_window, text="Register", command=lambda: self.register_user(entry_username.get(), entry_password.get()))
#         btn_register.pack(pady=10)

#     def register_user(self, username, password):
#         # Here you can implement your registration logic
#         # For demonstration purposes, just show a message box
#         messagebox.showinfo("Registration", f"Registered User: {username}")

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

#         # Add dashboard components based on user type

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     root = tk.Tk()
#     login_system = LoginSystem(root)
#     root.mainloop()

######################################################################################################################################################
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

        # Add buttons to access other functionalities
        if self.user_type == "student":
            pass  # Add student dashboard components
        elif self.user_type == "parent":
            pass  # Add parent dashboard components
        elif self.user_type == "teacher":
            btn_assignments = tk.Button(self.root, text="Assignment Manager",
                                        command=self.AssignmentManager)
            btn_assignments.pack(pady=5)

            btn_notice_board = tk.Button(self.root, text="NoticeBoardManager",
                                          command=self.NoticeBoardManager)
            btn_notice_board.pack(pady=5)

            btn_payment_system = tk.Button(self.root, text="Payment System",
                                            command=self.PaymentSystem)
            btn_payment_system.pack(pady=5)

            btn_attendance_manager = tk.Button(self.root, text="Attendance Manager",
                                               command=self.AttendanceManager)
            btn_attendance_manager.pack(pady=5)

    def AssignmentManager(self):
        from assign_manager import AssignmentManager
        assignment_window = tk.Tk()
        assignment_window.title("Assignment Manager")
        assignment_manager = assignment_manager.AssignmentManager(assignment_window)
        assignment_manager.run()
        

    def NoticeBoardManager(self):
        from teacher_notice import NoticeBoardManager
        notice_window = tk.Tk()
        notice_window.title("Notice Manager")
        notice_manager = notice_manager.NoticeBoardManager(notice_window)
        notice_manager.run()

    def PaymentSystem(self):
        from teacher_payments import PaymentSystem
        payment_window = tk.Tk()
        payment_window.title("Payment Manager")
        payment_manager = payment_manager.PaymentSystem(payment_window)
        payment_manager.run()

    def AttendanceManager(self):
        from teacher_student_attend import AttendanceManager
        attendance_window = tk.Tk()
        attendance_window.title("Attendance Manager") 
        attendance_manager = attendance_manager.AttendanceManager(attendance_window)
        attendance_manager.run()

    def run(self):
        self.root.mainloop()
