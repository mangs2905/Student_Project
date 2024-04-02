# import json
# from datetime import datetime

# class PaymentSystem:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.payments = self.load_payments()

#     def load_payments(self):
#         try:
#             with open(self.file_path, 'r') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return []

#     def save_payments(self):
#         with open(self.file_path, 'w') as file:
#             json.dump(self.payments, file, indent=4)

#     def add_payment(self, student_id, amount, date):
#         new_payment = {"student_id": student_id, "amount": amount, "date": date}
#         self.payments.append(new_payment)
#         self.save_payments()

#     def get_payments_for_month(self, year, month):
#         payments_in_month = []
#         for payment in self.payments:
#             payment_date = datetime.strptime(payment['date'], '%Y-%m-%d')
#             if payment_date.year == year and payment_date.month == month:
#                 payments_in_month.append(payment)
#         return payments_in_month

#     def calculate_total_payments_for_year(self, year):
#         total_payments = 0
#         for payment in self.payments:
#             payment_date = datetime.strptime(payment['date'], '%Y-%m-%d')
#             if payment_date.year == year:
#                 total_payments += payment['amount']
#         return total_payments

#     def generate_report(self, year, month=None):
#         if month:
#             payments = self.get_payments_for_month(year, month)
#         else:
#             payments = self.payments

#         report = f"Payment Report for {'Year' if not month else 'Month'} {year}\n"
#         for payment in payments:
#             report += f"Student ID: {payment['student_id']}, Amount: {payment['amount']}, Date: {payment['date']}\n"
#         return report

# # Example usage:
# if __name__ == "__main__":
#     # Create a payment system
#     payment_system = PaymentSystem('payments.json')

#     # Add payments
#     payment_system.add_payment('12345', 100, '2024-03-01')
#     payment_system.add_payment('67890', 200, '2024-03-15')
#     payment_system.add_payment('12345', 150, '2024-04-05')

#     # Generate report for March 2024
#     report_march = payment_system.generate_report(2024, 3)
#     print(report_march)

#     # Calculate total payments for 2024
#     total_payments_2024 = payment_system.calculate_total_payments_for_year(2024)
#     print("Total payments for 2024:", total_payments_2024)

#     # Generate report for the whole year 2024
#     report_2024 = payment_system.generate_report(2024)
#     print(report_2024)
######################################################################################################################################
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
from datetime import datetime

class PaymentSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.payments = self.load_payments()

    def load_payments(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_payments(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.payments, file, indent=4)

    def add_payment(self, student_id, amount, date):
        new_payment = {"student_id": student_id, "amount": amount, "date": date}
        self.payments.append(new_payment)
        self.save_payments()

    def get_payments_for_month(self, year, month):
        payments_in_month = []
        for payment in self.payments:
            payment_date = datetime.strptime(payment['date'], '%Y-%m-%d')
            if payment_date.year == year and payment_date.month == month:
                payments_in_month.append(payment)
        return payments_in_month

    def calculate_total_payments_for_year(self, year):
        total_payments = 0
        for payment in self.payments:
            payment_date = datetime.strptime(payment['date'], '%Y-%m-%d')
            if payment_date.year == year:
                total_payments += payment['amount']
        return total_payments

    def generate_report(self, year, month=None):
        if month:
            payments = self.get_payments_for_month(year, month)
        else:
            payments = self.payments

        report = f"Payment Report for {'Year' if not month else 'Month'} {year}\n"
        for payment in payments:
            report += f"Student ID: {payment['student_id']}, Amount: {payment['amount']}, Date: {payment['date']}\n"
        return report

class PaymentSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment System")
        self.root.geometry("400x300")

        self.payment_system = PaymentSystem('payments.json')

        self.label_title = tk.Label(root, text="Payment System", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        self.btn_add_payment = tk.Button(root, text="Add Payment", command=self.add_payment)
        self.btn_add_payment.pack(pady=5)

        self.btn_view_report = tk.Button(root, text="View Report", command=self.view_report)
        self.btn_view_report.pack(pady=5)

    def add_payment(self):
        student_id = simpledialog.askstring("Student ID", "Enter Student ID:")
        if student_id:
            amount = simpledialog.askfloat("Amount", "Enter Amount:")
            if amount:
                date = simpledialog.askstring("Date", "Enter Date (YYYY-MM-DD):")
                if date:
                    self.payment_system.add_payment(student_id, amount, date)
                    messagebox.showinfo("Success", "Payment added successfully.")

    def view_report(self):
        year = simpledialog.askinteger("Year", "Enter Year:")
        if year:
            month = simpledialog.askinteger("Month", "Enter Month (optional, leave blank for full year report):")
            report = self.payment_system.generate_report(year, month)
            messagebox.showinfo("Payment Report", report)

if __name__ == "__main__":
    root = tk.Tk()
    payment_system_gui = PaymentSystemGUI(root)
    root.mainloop()
