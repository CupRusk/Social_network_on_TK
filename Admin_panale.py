# print LABUBU SOSAL\\
def init_admin_win():
    import tkinter as tk 
    # from tg_bot import init_bot as bot_ini   

    window = tk.Tk() 
    window.title("Админ панель Социальной сети: МЫ БОГИ")
    window.geometry("800x600")
    window.configure(bg="white")

    title_label = tk.Label(window, text="Админ панель Социальной сети: МЫ БОГИ", font=("Arial", 16), bg="lightblue", pady=10, foreground="black")
    title_label.pack()

    # Button_active = tk.Button(window, text="Активировать бота", font=("Arial", 14), command=init_bot, bg="green", fg="white", padx=10, pady=5)
    # Button_active.pack(pady=20)

    window.mainloop()