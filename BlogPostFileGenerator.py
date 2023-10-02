import tkinter as tk
from tkinter import filedialog
import os
import datetime

def save_file():
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d") + ".md"
    file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown Files", "*.md")], initialfile=file_name)
    if file_path:
        with open(file_path, "w") as f:
            f.write(f"---\nlayout: page\ntitle: {title_entry.get()}\npermalink: /{permalink_entry.get()}/\n---\n\n{editor.get('1.0', 'end')}")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".md", filetypes=[("Markdown Files", "*.md")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
            header, body = content.split("\n---\n")
            header_lines = header.split("\n")
            title = header_lines[2].split(": ")[1]
            permalink = header_lines[3].split(": ")[1]
            title_entry.delete(0, tk.END)
            title_entry.insert(0, title)
            permalink_entry.delete(0, tk.END)
            permalink_entry.insert(0, permalink)
            editor.delete("1.0", tk.END)
            editor.insert("1.0", body)

root = tk.Tk()
root.title("Markdown Editor")

# Header Frame
header_frame = tk.Frame(root)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="Title:")
title_label.pack(side="left")

title_entry = tk.Entry(header_frame)
title_entry.pack(side="left", fill="x", expand=True)

permalink_label = tk.Label(header_frame, text="Permalink:")
permalink_label.pack(side="left")

permalink_entry = tk.Entry(header_frame)
permalink_entry.pack(side="left", fill="x", expand=True)

# Editor Frame
editor_frame = tk.Frame(root)
editor_frame.pack(fill="both", expand=True)

editor = tk.Text(editor_frame)
editor.pack(fill="both", expand=True)

# Save Button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side="right")

# Open Button
open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack(side="right", padx=5)

root.mainloop()

