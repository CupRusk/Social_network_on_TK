import tkinter as tk
import multiprocessing
from BOT.tg_bot import init_bot
from window.valid_token import validate_token

def init_admin_win():
    token = ""
    bot_process = None

    window = tk.Tk()
    window.title("Админ панель")
    window.geometry("400x200")

    welcome_label = tk.Label(window, text="Привет! Админ панель для вас!", font=("Arial", 14))
    welcome_label.pack(pady=10)

    entry_field = tk.Entry(window, width=30)
    entry_field.pack(pady=10)

    bot_button = tk.Button(window, text="Запустить бота", state="disabled")
    bot_button.pack(pady=20)

    def update_status(text: str):
        welcome_label.config(text=text)

    def toggle_bot():
        nonlocal bot_process
        if bot_process and bot_process.is_alive():
            bot_process.terminate()
            bot_process = None
            bot_button.config(text="Запустить бота")
            update_status("Бот остановлен!")
        else:
            if not validate_token(token):
                update_status("Невалидный токен")
                return
            bot_process = multiprocessing.Process(target=init_bot, args=(token,))
            bot_process.start()
            bot_button.config(text="Выключить бота")
            update_status("Бот запущен!")

    def set_token():
        nonlocal token
        token = entry_field.get()
        if validate_token(token):
            update_status("Токен установлен")
            bot_button.config(state="normal")
        else:
            update_status("Невалидный токен")

    token_button = tk.Button(window, text="Установить токен", command=set_token)
    token_button.pack(pady=5)

    bot_button.config(command=toggle_bot)

    def on_closing():
        nonlocal bot_process
        if bot_process and bot_process.is_alive():
            bot_process.terminate()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
