import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from downloader import download_video


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)


def start_download():
    url = url_entry.get()
    save_path = folder_path.get()
    resolution = resolution_var.get()
    audio_only = audio_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    if not save_path:
        messagebox.showerror("Error", "Please select a save location.")
        return

    status_label.config(text="Downloading...")
    root.update_idletasks()

    result = download_video(url, save_path, resolution, audio_only)

    status_label.config(text=result)
    messagebox.showinfo("Download Status", result)


# GUI Setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x350")

# URL Input
tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Save Location
tk.Label(root, text="Save Location:").pack(pady=5)
folder_path = tk.StringVar()
tk.Entry(root, textvariable=folder_path, width=40).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Browse", command=browse_folder).pack(side=tk.LEFT)

# Video Quality Selection
tk.Label(root, text="Select Quality:").pack(pady=5)
resolution_var = tk.StringVar(value="highest")
quality_options = ["highest", "720p", "480p", "360p", "240p", "144p"]
ttk.Combobox(root, textvariable=resolution_var, values=quality_options, state="readonly").pack()

# Audio-Only Option
audio_var = tk.BooleanVar()
tk.Checkbutton(root, text="Download Audio Only", variable=audio_var).pack()

# Download Button
tk.Button(root, text="Download", command=start_download).pack(pady=20)

# Status Label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

root.mainloop()
