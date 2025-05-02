import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TODO LIST")
root.geometry("400x500")
root.resizable(True, True)  # Make window resizable

task_vars = []

# Function to update progress bar
def update_progress():
    completed = sum(var.get() for var in task_vars)
    total = len(task_vars)
    progress_bar['value'] = (completed / total) * 100 if total else 0

# Function to add a single task
def add_single_task(task_text):
    var = tk.IntVar()
    cb = tk.Checkbutton(task_container, text=task_text.strip(), variable=var, command=update_progress)
    cb.pack(anchor='w', pady=2)
    task_vars.append(var)
    update_progress()

# Function to handle multiple pasted tasks
def add_tasks_from_input():
    raw_text = task_input.get("1.0", tk.END)
    tasks = [task.strip() for task in raw_text.splitlines() if task.strip()]
    for task in tasks:
        add_single_task(task)
    task_input.delete("1.0", tk.END)

# Title and instruction
tk.Label(root, text="TODO LIST", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, text="Paste all your tasks below (one per line):").pack()

# Input field for pasting tasks
task_input = tk.Text(root, height=5, width=45)
task_input.pack(pady=5)

tk.Button(root, text="Add Tasks", command=add_tasks_from_input).pack(pady=5)

# Scrollable frame for checkboxes
task_frame = tk.Frame(root)
task_frame.pack(fill='both', expand=True, padx=10, pady=10)

canvas = tk.Canvas(task_frame)
scrollbar = ttk.Scrollbar(task_frame, orient='vertical', command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

task_container = scrollable_frame

# Progress bar at the bottom
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.pack(pady=15)

# Run the app
root.mainloop()
