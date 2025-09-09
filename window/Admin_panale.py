import tkinter as tk
from BOT.tg_bot import init_bot
import multiprocessing

def init_admin_win():
    window = tk.Tk()
    window.title("Админ панель")
    window.geometry("800x600")

    def start_bot_process():
        p = multiprocessing.Process(target=init_bot)
        p.start()

    button = tk.Button(window, text="Запустить бота", command=start_bot_process)
    button.pack(pady=20)

    window.mainloop()
