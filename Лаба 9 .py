import tkinter as tk
from tkinter import messagebox

user_database = {}
def register():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if username in user_database:
            messagebox.showerror("Ошибка регистрации", "Пользователь с таким именем уже существует.")
        else:
            user_database[username] = password
            messagebox.showinfo("Регистрация успешна", "Вы успешно зарегистрированы!")
            clear_entries()
    else:
        messagebox.showwarning("Ошибка регистрации", "Пожалуйста, заполните все поля.")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if username in user_database and user_database[username] == password:
            messagebox.showinfo("Вход выполнен успешно", f"Добро пожаловать, {username}!")
        else:
            messagebox.showerror("Ошибка входа", "Неправильное имя пользователя или пароль.")
    else:
        messagebox.showwarning("Ошибка входа", "Пожалуйста, заполните все поля.")

def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Регистрация и Вход")

username_label = tk.Label(root, text="Имя пользователя:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Пароль:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

register_button = tk.Button(root, text="Регистрация", command=register)
register_button.pack()

login_button = tk.Button(root, text="Вход", command=login)
login_button.pack()

root.mainloop()
