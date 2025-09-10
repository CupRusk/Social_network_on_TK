import tkinter as tk
import multiprocessing
import asyncio
from BOT.tg_bot import init_bot
# TODO: Сделать валидацию токенов, если токен например не правильный - выход с запуска.

def init_admin_win():
    token = "ваш_токен"
    status_bot = False
    bot_process = None

    window = tk.Tk()
    window.title("Админ панель")
    window.geometry("400x200")

    Welcome_label = tk.Label(window, text="Привет! Админ панель для вас!", font=("Arial", 14))
    Welcome_label.pack(pady=10)

    entry_field = tk.Entry(window, width=30)
    entry_field.pack(pady=10)

    def rename_Hello(new_text):
        Welcome_label.config(text=new_text)

    def start_bot_process():
        nonlocal status_bot, bot_process

        if bot_process is None or not bot_process.is_alive():
            bot_process = multiprocessing.Process(target=init_bot, args=(token,))
            bot_process.start()
            status_bot = True
            bot_button.config(text="Выключить бота", command=stop_bot_process)
            rename_Hello("Бот запущен!")

    def stop_bot_process():
        nonlocal status_bot, bot_process
        if bot_process and bot_process.is_alive():
            bot_process.terminate()
        status_bot = False
        bot_button.config(text="Запустить бота", command=start_bot_process)
        rename_Hello("Бот остановлен!")

    def input_token():
        nonlocal token
        token = entry_field.get()
        rename_Hello("Токен установлен")
        bot_button.config(state="normal")

    token_button = tk.Button(window, text="Установить токен", command=input_token)
    token_button.pack(pady=5)

    bot_button = tk.Button(window, text="Запустить бота", command=start_bot_process, state="disabled")
    bot_button.pack(pady=20)

    def on_closing():
        nonlocal bot_process
        if bot_process and bot_process.is_alive():
            bot_process.terminate()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
