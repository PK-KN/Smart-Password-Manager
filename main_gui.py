import tkinter as tk
from tkinter import messagebox
# Import functions from our utility file
from security_utils import get_cipher, generate_random_password, check_pwd_strength


def on_generate():
    new_pwd = generate_random_password()
    entry_pwd.delete(0, tk.END)
    entry_pwd.insert(0, new_pwd)
    update_strength_label()


def update_strength_label(event=None):
    text, color = check_pwd_strength(entry_pwd.get())
    lbl_strength.config(text=text, fg=color)


def on_save():
    master = entry_master.get()
    acc = entry_acc.get()
    pwd = entry_pwd.get()

    if not (master and acc and pwd):
        messagebox.showwarning("Error", "Please fill all fields")
        return

    try:
        cipher = get_cipher(master)
        encrypted = cipher.encrypt(pwd.encode()).decode()
        with open("passwords.txt", "a") as f:
            f.write(f"{acc}|{encrypted}\n")
        messagebox.showinfo("Success", "Password secured and saved!")
    except Exception as e:
        messagebox.showerror("Error", "Encryption failed!")


# --- UI Setup ---
root = tk.Tk()
root.title("SecurePass Pro")
root.geometry("350x450")

tk.Label(root, text="Master Key:", font=("Arial", 10, "bold")).pack(pady=5)
entry_master = tk.Entry(root, show="*")
entry_master.pack()

tk.Label(root, text="Account Name:").pack(pady=5)
entry_acc = tk.Entry(root)
entry_acc.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_pwd = tk.Entry(root)
entry_pwd.bind("<KeyRelease>", update_strength_label)
entry_pwd.pack()

lbl_strength = tk.Label(root, text="")
lbl_strength.pack()

tk.Button(root, text="Generate Strong Pwd", command=on_generate).pack(pady=10)
tk.Button(root, text="Save Encrypted Data", command=on_save,
          bg="blue", fg="white").pack(pady=20)

root.mainloop()
