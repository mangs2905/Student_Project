
# import json

# class UserManagement:
#     def __init__(self):
#         self.users = {}

#     def register_user(self, username, password, user_type):
#         if user_type not in self.users:
#             self.users[user_type] = {}
#         self.users[user_type][username] = password

#     def save_users(self):
#         for user_type, user_data in self.users.items():
#             filename = f"{user_type}_users.json"
#             with open(filename, "w") as f:
#                 json.dump(user_data, f)

#     def load_users(self):
#         for user_type in ["teacher", "student", "parent"]:
#             filename = f"{user_type}_users.json"
#             try:
#                 with open(filename, "r") as f:
#                     self.users[user_type] = json.load(f)
#             except FileNotFoundError:
#                 # If the file doesn't exist, initialize an empty dictionary
#                 self.users[user_type] = {}

#     def authenticate_user(self, username, password, user_type):
#         if user_type in self.users and username in self.users[user_type]:
#             return self.users[user_type][username] == password
#         return False

# # Example usage:
# user_management = UserManagement()
# user_management.load_users()

# # Register a new user
# user_management.register_user("new_student", "new_password", "student")
# user_management.save_users()

# # Authenticate a user
# username = "new_student"
# password = "new_password"
# user_type = "student"
# if user_management.authenticate_user(username, password, user_type):
#     print("Authentication successful!")
# else:
#     print("Authentication failed!")

########################################################################################################################

import tkinter as tk
from tkinter import messagebox
import webbrowser
import json

class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, user_type):
        if user_type not in self.users:
            self.users[user_type] = {}
        self.users[user_type][username] = password

    def save_users(self):
        for user_type, user_data in self.users.items():
            filename = f"{user_type}_users.json"
            with open(filename, "w") as f:
                json.dump(user_data, f)

    def load_users(self):
        for user_type in ["teacher", "student", "parent"]:
            filename = f"{user_type}_users.json"
            try:
                with open(filename, "r") as f:
                    self.users[user_type] = json.load(f)
            except FileNotFoundError:
                # If the file doesn't exist, initialize an empty dictionary
                self.users[user_type] = {}

    def authenticate_user(self, username, password, user_type):
        if user_type in self.users and username in self.users[user_type]:
            return self.users[user_type][username] == password
        return False

class RegistrationWindow:
    def __init__(self, root, user_management):
        self.root = root
        self.user_management = user_management
        self.root.title("Sign Up")
        self.root.geometry("300x200")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.btn_signup = tk.Button(root, text="Sign Up", command=self.sign_up)
        self.btn_signup.pack(pady=5)

        self.btn_google_signup = tk.Button(root, text="Sign Up using Google", command=self.sign_up_with_google)
        self.btn_google_signup.pack(pady=5)

        self.btn_login = tk.Button(root, text="Login", command=self.open_login_window)
        self.btn_login.pack(pady=5)

    def sign_up(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user_type = "student"  # Change this according to user selection

        if username and password:
            self.user_management.register_user(username, password, user_type)
            self.user_management.save_users()
            messagebox.showinfo("Success", "Registration successful!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Username and password are required.")

    def sign_up_with_google(self):
        webbrowser.open("https://accounts.google.com/signup")

    def open_login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("300x200")
        login_frame = LoginFrame(login_window, self.user_management, self.root)
        login_frame.pack()

class LoginFrame(tk.Frame):
    def __init__(self, parent, user_management, main_window):
        super().__init__(parent)
        self.user_management = user_management
        self.main_window = main_window

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(self, text="Login", command=self.login)
        self.btn_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user_type = "student"  # Change this according to user selection

        if self.user_management.authenticate_user(username, password, user_type):
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            # Close the login window
            self.master.destroy()
            # Open the main dashboard window
            self.main_window.deiconify()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Project")
        self.geometry("400x300")
        self.withdraw()  # Hide the window initially

        # Create buttons for dashboard actions
        self.btn_notice_board = tk.Button(self, text="Notice Board", command=self.open_notice_board)
        self.btn_notice_board.pack(pady=5)

        self.btn_attendance_manager = tk.Button(self, text="Attendance Manager", command=self.open_attendance_manager)
        self.btn_attendance_manager.pack(pady=5)

        self.btn_assignment_manager = tk.Button(self, text="Assignment Manager", command=self.open_assignment_manager)
        self.btn_assignment_manager.pack(pady=5)

    def open_notice_board(self):
        # Placeholder function to open notice board window
        messagebox.showinfo("Notice Board", "This feature is under development.")

    def open_attendance_manager(self):
        # Placeholder function to open attendance manager window
        messagebox.showinfo("Attendance Manager", "This feature is under development.")

    def open_assignment_manager(self):
        # Placeholder function to open assignment manager window
        messagebox.showinfo("Assignment Manager", "This feature is under development.")

if __name__ == "__main__":
    root = tk.Tk()
    user_management = UserManagement()
    user_management.load_users()
    registration_window = RegistrationWindow(root, user_management)

    # Create the main dashboard window
    dashboard = Dashboard()
    registration_window.root.mainloop()
