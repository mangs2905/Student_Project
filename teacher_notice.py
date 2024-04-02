
import tkinter as tk
from tkinter import messagebox
import json

class NoticeBoardManager:
    def __init__(self):
        self.notice_board_file = "notice_board.json"
        self.load_notice_board()

    def load_notice_board(self):
        try:
            with open(self.notice_board_file, "r") as file:
                self.notice_board_data = json.load(file)
        except FileNotFoundError:
            self.notice_board_data = {}

    def save_notice_board(self):
        with open(self.notice_board_file, "w") as file:
            json.dump(self.notice_board_data, file, indent=4)

    def add_notice(self, date, notice):
        if date not in self.notice_board_data:
            self.notice_board_data[date] = []
        self.notice_board_data[date].append(notice)
        self.save_notice_board()

    def delete_notice(self, date, index):
        if date in self.notice_board_data and index < len(self.notice_board_data[date]):
            del self.notice_board_data[date][index]
            self.save_notice_board()
            messagebox.showinfo("Success", "Notice deleted successfully.")
        else:
            messagebox.showerror("Error", "Notice not found for the given date and index.")

    def view_notice_board(self, date=None):
        if date is None:
            notice_board_str = "Notice Board:\n\n"
            for date, notices in self.notice_board_data.items():
                notice_board_str += f"Date: {date}\n"
                for idx, notice in enumerate(notices):
                    notice_board_str += f"{idx + 1}. {notice}\n"
                notice_board_str += "\n"
            messagebox.showinfo("Notice Board", notice_board_str)
        else:
            if date in self.notice_board_data:
                notice_board_str = f"Notice Board for {date}:\n\n"
                for idx, notice in enumerate(self.notice_board_data[date]):
                    notice_board_str += f"{idx + 1}. {notice}\n"
                messagebox.showinfo("Notice Board", notice_board_str)
            else:
                messagebox.showinfo("Notice Board", "No notices found for the given date.")

    def upload_timetable(self, date, timetable):
        self.notice_board_data[date] = ["Timetable:"] + timetable
        self.save_notice_board()
        messagebox.showinfo("Success", "Timetable uploaded successfully.")

class NoticeBoardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Notice Board Manager")
        self.root.geometry("400x300")

        self.notice_board_manager = NoticeBoardManager()

        self.label_title = tk.Label(root, text="Notice Board Manager", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        self.btn_view_notice_board = tk.Button(root, text="View Notice Board", command=self.view_notice_board)
        self.btn_view_notice_board.pack(pady=5)

        self.btn_upload_timetable = tk.Button(root, text="Upload Timetable", command=self.upload_timetable)
        self.btn_upload_timetable.pack(pady=5)

    def view_notice_board(self):
        self.notice_board_manager.view_notice_board()

    def upload_timetable(self):
        # A simple dialog to input date and timetable
        date = simpledialog.askstring("Date", "Enter the date (YYYY-MM-DD):")
        if date:
            timetable_str = simpledialog.askstring("Timetable", "Enter the timetable (separated by commas):")
            if timetable_str:
                timetable = timetable_str.split(",")
                self.notice_board_manager.upload_timetable(date, timetable)

if __name__ == "__main__":
    root = tk.Tk()
    notice_board_gui = NoticeBoardGUI(root)
    root.mainloop()
