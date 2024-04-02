# import json

# class AssignmentManager:
#     def __init__(self):
#         self.assignments = []

#     def load_assignments(self, filename):
#         try:
#             with open(filename, 'r') as file:
#                 self.assignments = json.load(file)
#         except FileNotFoundError:
#             self.assignments = []

#     def save_assignments(self, filename):
#         with open(filename, 'w') as file:
#             json.dump(self.assignments, file, indent=4)

#     def add_assignment(self, student_id, assignment_name, submission_date):
#         self.assignments.append({
#             "student_id": student_id,
#             "assignment_name": assignment_name,
#             "submission_date": submission_date,
#             "marks": None,
#             "remarks": None
#         })

#     def get_assignments_by_student(self, student_id):
#         return [assignment for assignment in self.assignments if assignment["student_id"] == student_id]

#     def grade_assignment(self, student_id, assignment_name, marks, remarks):
#         for assignment in self.assignments:
#             if assignment["student_id"] == student_id and assignment["assignment_name"] == assignment_name:
#                 assignment["marks"] = marks
#                 assignment["remarks"] = remarks
#                 break

# # Example usage
# if __name__ == "__main__":
#     # Initialize AssignmentManager
#     assignment_manager = AssignmentManager()

#     # Load assignments from file
#     assignment_manager.load_assignments("assignments.json")

#     # Add assignment
#     assignment_manager.add_assignment("1001", "Math Assignment", "2023-03-15")

#     # Get assignments for a student
#     student_id = "1001"
#     student_assignments = assignment_manager.get_assignments_by_student(student_id)
#     print(f"Assignments for student {student_id}:")
#     for assignment in student_assignments:
#         print(assignment)

#     # Grade an assignment
#     assignment_manager.grade_assignment("1001", "Math Assignment", marks=90, remarks="Well done!")

#     # Save assignments to file
#     assignment_manager.save_assignments("assignments.json")
#################################################################################################################################

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

class AssignmentManager:
    def __init__(self):
        self.assignments = []

    def load_assignments(self, filename):
        try:
            with open(filename, 'r') as file:
                self.assignments = json.load(file)
        except FileNotFoundError:
            self.assignments = []

    def save_assignments(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.assignments, file, indent=4)

    def add_assignment(self, student_id, assignment_name, submission_date):
        self.assignments.append({
            "student_id": student_id,
            "assignment_name": assignment_name,
            "submission_date": submission_date,
            "marks": None,
            "remarks": None
        })

    def get_assignments_by_student(self, student_id):
        return [assignment for assignment in self.assignments if assignment["student_id"] == student_id]

    def grade_assignment(self, student_id, assignment_name, marks, remarks):
        for assignment in self.assignments:
            if assignment["student_id"] == student_id and assignment["assignment_name"] == assignment_name:
                assignment["marks"] = marks
                assignment["remarks"] = remarks
                break

class AssignmentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Assignment Manager")
        self.root.geometry("400x300")

        self.assignment_manager = AssignmentManager()

        self.label_title = tk.Label(root, text="Assignment Manager", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        self.label_student_id = tk.Label(root, text="Student ID:")
        self.label_student_id.pack(pady=5)
        self.entry_student_id = tk.Entry(root)
        self.entry_student_id.pack()

        self.label_assignment_name = tk.Label(root, text="Assignment Name:")
        self.label_assignment_name.pack(pady=5)
        self.entry_assignment_name = tk.Entry(root)
        self.entry_assignment_name.pack()

        self.label_submission_date = tk.Label(root, text="Submission Date (YYYY-MM-DD):")
        self.label_submission_date.pack(pady=5)
        self.entry_submission_date = tk.Entry(root)
        self.entry_submission_date.pack()

        self.label_marks = tk.Label(root, text="Marks:")
        self.label_marks.pack(pady=5)
        self.entry_marks = tk.Entry(root)
        self.entry_marks.pack()

        self.label_remarks = tk.Label(root, text="Remarks:")
        self.label_remarks.pack(pady=5)
        self.entry_remarks = tk.Entry(root)
        self.entry_remarks.pack()

        self.btn_submit_assignment = tk.Button(root, text="Submit Assignment", command=self.submit_assignment)
        self.btn_submit_assignment.pack(pady=10)

    def submit_assignment(self):
        student_id = self.entry_student_id.get()
        assignment_name = self.entry_assignment_name.get()
        submission_date = self.entry_submission_date.get()
        marks = self.entry_marks.get()
        remarks = self.entry_remarks.get()

        # Validate input
        if not student_id or not assignment_name or not submission_date or not marks or not remarks:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Check if submission date is valid
        try:
            datetime.strptime(submission_date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid submission date format. Please use YYYY-MM-DD")
            return

        # Add assignment
        self.assignment_manager.add_assignment(student_id, assignment_name, submission_date)
        self.assignment_manager.grade_assignment(student_id, assignment_name, marks, remarks)
        self.assignment_manager.save_assignments("assignments.json")

        messagebox.showinfo("Success", "Assignment submitted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    assignment_gui = AssignmentGUI(root)
    root.mainloop()
