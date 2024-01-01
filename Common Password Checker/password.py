import tkinter as tk
from tkinter import messagebox

def check_password(password):
    with open("pwd.txt") as file:
        common_password = file.read().splitlines()
        
    for i, common_pwd in enumerate(common_password, start=1):
        if password == common_pwd:
            messagebox.showinfo(
                "Password Check", f"{password} : not unique (#{i})")
            return
        
    messagebox.showinfo("Password Check ", f"{password} : unique" )
    
def main():
    app = tk.Tk()
    app.title("Password Checker")
    app.geometry("800x600")
    app.configure(bg="black")
    
    label = tk.Label(app, text="Enter password : ", fg="white", bg="black")
    label.pack()
    
    password_entry = tk.Entry(app, show=" ")
    password_entry.pack()
    
    check_button = tk.Button(
        app, text="Check", command=lambda : check_password(password_entry.get()))
    check_button.pack()
    
    app.mainloop()
    
if __name__ == "__main__":
    main()