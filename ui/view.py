
import tkinter as tk

class LoggerView:
    def __init__(self, on_start_voice_callback):
        self.root = tk.Tk()
        self.root.title("GeoIntel Voice Logger")
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        self.button = tk.Button(self.root, text="Start Voice Input", command=on_start_voice_callback)
        self.button.pack(pady=5)

    def update_log_display(self, text):
        self.text_area.insert(tk.END, f"{text}\n")
        self.text_area.see(tk.END)

    def run(self):
        self.root.mainloop()
