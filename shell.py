import tkinter as tk
from Configuration_management_practice_1.commands import ls, cd, pwd, cat, wc

class ShellGUI(tk.Tk):
    def __init__(self, user_name, computer_name, vfs):
        super().__init__()
        self.user_name = user_name
        self.computer_name = computer_name
        self.vfs = vfs
        self.title("Shell Emulator")
        self.geometry("700x500")

        # Поле для вывода результатов
        self.text_area = tk.Text(self, height=20, width=80)
        self.text_area.pack(pady=10)

        # Поле для ввода команд
        self.entry = tk.Entry(self, width=80)
        self.entry.pack(pady=10)

        # Привязка Enter для ввода команд через поле
        self.bind("<Return>", self.execute_command)

        # Начальный вывод
        self.update_prompt()

    def update_prompt(self):
        self.text_area.insert(tk.END, f"{self.user_name}@{self.computer_name}:{self.vfs.get_pwd()}$ ")

    def execute_command(self, event):
        input_text = self.entry.get()
        command, *args = input_text.split()
        self.entry.delete(0, tk.END)

        if command == "ls":
            self.run_ls()
        elif command == "cd":
            if args:
                self.run_cd(args[0])
            else:
                self.text_area.insert(tk.END, "\nDirectory not specified\n")
        elif command == "pwd":
            self.run_pwd()
        elif command == "cat":
            if args:
                self.run_cat(args[0])
            else:
                self.text_area.insert(tk.END, "\nFile not specified\n")
        elif command == "wc":
            if args:
                self.run_wc(args[0])
            else:
                self.text_area.insert(tk.END, "\nFile not specified\n")
        elif command == "exit":
            self.quit()
        else:
            self.text_area.insert(tk.END, "\nCommand not found\n")

        self.update_prompt()

    def run_ls(self):
        output = ls(self.vfs)
        self.text_area.insert(tk.END, "\n" + "\n".join(output) + "\n")

    def run_pwd(self):
        output = pwd(self.vfs)
        self.text_area.insert(tk.END, "\n" + output + "\n")

    def run_cd(self, directory=None):
        if directory:
            cd(self.vfs, directory)
        else:
            cd(self.vfs, self.entry.get())
        self.update_prompt()

    def run_cat(self, filename=None):
        if filename:
            output = cat(self.vfs, filename)
        else:
            output = cat(self.vfs, self.entry.get())
        self.text_area.insert(tk.END, "\n" + output + "\n")

    def run_wc(self, filename=None):
        if filename:
            lines, words, chars = wc(self.vfs, filename)
        else:
            lines, words, chars = wc(self.vfs, self.entry.get())
        output = f"{lines} {words} {chars}"
        self.text_area.insert(tk.END, "\n" + output + "\n")
