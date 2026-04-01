import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Hello", "The Gemini CLI Skill launched this GUI successfully!")

def main():
    root = tk.Tk()
    root.title("Gemini CLI Skill Demo")
    root.geometry("300x200")

    label = tk.Label(root, text="Python GUI Setup Launcher Demo", pady=20)
    label.pack()

    btn = tk.Button(root, text="Click Me", command=on_click)
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
