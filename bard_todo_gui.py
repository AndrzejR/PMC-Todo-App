import tkinter as tk


class TodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple To-Do App")
        self.todo_list = []

        # Create input frame for adding new tasks
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT)
        self.task_entry.bind("<Return>", self.add_task)

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT)

        # Create listbox for displaying tasks
        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.pack()
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)

        # Create button for clearing all tasks
        clear_button = tk.Button(self.root, text="Clear All", command=self.clear_tasks)
        clear_button.pack()

    def run(self):
        self.root.mainloop()

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.todo_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self, event):
        try:
            index = self.task_listbox.curselection()[0]
            completed_task = self.task_listbox.get(index)
            self.todo_list.remove(completed_task)
            self.task_listbox.delete(index)
        except IndexError:
            pass  # No task selected

    def clear_tasks(self):
        self.todo_list = []
        self.task_listbox.delete(0, tk.END)


if __name__ == "__main__":
    app = TodoApp()
    app.run()
