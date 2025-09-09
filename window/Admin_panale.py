import tkinter as tk
import threading
from BOT.tg_bot import init_bot


def init_admin_win():
    window = tk.Tk()
    window.title("Админ панель Социальной сети: МЫ БОГИ")
    window.geometry("800x600")
    window.configure(bg="white")

    title_label = tk.Label(
        window,
        text="Админ панель Социальной сети: МЫ БОГИ",
        font=("Arial", 16),
        bg="lightblue",
        pady=10,
        foreground="black"
    )
    title_label.pack()

    def start_bot():
        threading.Thread(target=init_bot, daemon=True).start()

    Button_active = tk.Button(
        window,
        text="Активировать бота",
        font=("Arial", 14),
        command=start_bot,
        bg="green",
        fg="white",
        padx=10,
        pady=5
    )
    Button_active.pack(pady=20)

    window.mainloop()
