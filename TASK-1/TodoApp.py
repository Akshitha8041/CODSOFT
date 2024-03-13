
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.due_date_entry = tk.Entry(root, width=20)
        self.due_date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.due_date_entry.insert(tk.END, "YYYY-MM-DD")

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.grid(row=2, column=0, padx=10, pady=10)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=10, pady=10)

        notify_button = tk.Button(root, text="Notify", command=self.notify_due_tasks)
        notify_button.grid(row=2, column=2, padx=10, pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        due_date_str = self.due_date_entry.get()

        if task and due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Warning", "Invalid date format. Use YYYY-MM-DD.")
                return

            self.tasks.append({"task": task, "due_date": due_date})
            self.task_listbox.insert(tk.END, f"{task} (Due: {due_date_str})")
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.due_date_entry.insert(tk.END, "YYYY-MM-DD")
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter both task and due date.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = self.task_entry.get()
            updated_due_date_str = self.due_date_entry.get()

            if updated_task and updated_due_date_str:
                try:
                    updated_due_date = datetime.strptime(updated_due_date_str, "%Y-%m-%d")
                except ValueError:
                    messagebox.showwarning("Warning", "Invalid date format. Use YYYY-MM-DD.")
                    return

                self.tasks[selected_index[0]]["task"] = updated_task
                self.tasks[selected_index[0]]["due_date"] = updated_due_date

                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"{updated_task} (Due: {updated_due_date_str})")

                self.task_entry.delete(0, tk.END)
                self.due_date_entry.delete(0, tk.END)
                self.due_date_entry.insert(tk.END, "YYYY-MM-DD")
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter both task and due date.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def notify_due_tasks(self):
        today = datetime.today().date()

        for task in self.tasks:
            due_date = task["due_date"].date()
            if due_date == today + timedelta(days=1):
                messagebox.showinfo("Notification", f"{task['task']} is due tomorrow!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = []
                lines = file.read().splitlines()
                for line in lines:
                    task, due_date_str = line.split("|")
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                    self.tasks.append({"task": task, "due_date": due_date})
                    self.task_listbox.insert(tk.END, f"{task} (Due: {due_date_str})")
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['due_date'].strftime('%Y-%m-%d')}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
