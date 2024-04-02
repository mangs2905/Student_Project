
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

class AttendanceManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Manager")
        self.root.geometry("400x300")

        self.attendance_manager = AttendanceManager()

        self.label_title = tk.Label(root, text="Attendance Manager", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        self.btn_view_attendance = tk.Button(root, text="View Attendance", command=self.view_attendance)
        self.btn_view_attendance.pack(pady=5)

        self.btn_add_attendance = tk.Button(root, text="Add Attendance", command=self.add_attendance)
        self.btn_add_attendance.pack(pady=5)

        self.btn_delete_attendance = tk.Button(root, text="Delete Attendance", command=self.delete_attendance)
        self.btn_delete_attendance.pack(pady=5)

        self.btn_view_graph = tk.Button(root, text="View Attendance Graph", command=self.view_graph)
        self.btn_view_graph.pack(pady=5)

        self.btn_check_leave = tk.Button(root, text="Check Leave", command=self.check_leave)
        self.btn_check_leave.pack(pady=5)

    def view_attendance(self):
        attendance_records = self.attendance_manager.view_attendance()
        messagebox.showinfo("Attendance Records", attendance_records)

    def add_attendance(self):
        date = self.get_date_input("Enter Date (YYYY-MM-DD):")
        if date:
            students_present = self.get_student_input("Enter Students Present (comma-separated):")
            if students_present:
                self.attendance_manager.add_attendance(date, students_present)
                messagebox.showinfo("Success", "Attendance added successfully.")

    def delete_attendance(self):
        date = self.get_date_input("Enter Date to Delete (YYYY-MM-DD):")
        if date:
            self.attendance_manager.delete_attendance(date)
            messagebox.showinfo("Success", f"Attendance for {date} deleted successfully.")

    def view_graph(self):
        self.attendance_manager.generate_attendance_graph()

    def check_leave(self):
        date = self.get_date_input("Enter Date to Check Leave (YYYY-MM-DD):")
        if date:
            leave_students = self.attendance_manager.check_leave(date)
            messagebox.showinfo("Students on Leave", f"Students on leave on {date}: {', '.join(leave_students)}")

    def get_date_input(self, prompt):
        return tk.simpledialog.askstring("Date Input", prompt)

    def get_student_input(self, prompt):
        return tk.simpledialog.askstring("Student Input", prompt)

class AttendanceManager:
    def __init__(self):
        self.attendance_file = "attendance.json"
        self.load_attendance()

    def load_attendance(self):
        try:
            with open(self.attendance_file, "r") as file:
                self.attendance_data = json.load(file)
        except FileNotFoundError:
            self.attendance_data = {}

    def save_attendance(self):
        with open(self.attendance_file, "w") as file:
            json.dump(self.attendance_data, file, indent=4)

    def view_attendance(self):
        attendance_records = "Attendance Records:\n"
        for date, attendance in self.attendance_data.items():
            attendance_records += f"Date: {date}, Attendance: {attendance}\n"
        return attendance_records

    def add_attendance(self, date, students_present):
        self.attendance_data[date] = students_present
        self.save_attendance()

    def delete_attendance(self, date):
        if date in self.attendance_data:
            del self.attendance_data[date]
            self.save_attendance()

    def generate_attendance_graph(self):
        dates = list(self.attendance_data.keys())
        attendance = [len(students) for students in self.attendance_data.values()]

        df = pd.DataFrame({"Date": dates, "Attendance": attendance})
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        df.resample("W").mean().plot(kind="bar", legend=False)
        plt.title("Weekly Attendance Statistics")
        plt.xlabel("Week")
        plt.ylabel("Average Attendance")
        plt.show()

        df.resample("M").mean().plot(kind="bar", legend=False)
        plt.title("Monthly Attendance Statistics")
        plt.xlabel("Month")
        plt.ylabel("Average Attendance")
        plt.show()

    def check_leave(self, date):
        if date in self.attendance_data:
            present_students = self.attendance_data[date]
            return [student for student in present_students if student.startswith("Leave:")]
        else:
            return []

if __name__ == "__main__":
    root = tk.Tk()
    attendance_manager_gui = AttendanceManagerGUI(root)
    root.mainloop()
