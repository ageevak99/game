import tkinter as tk, random
root = tk.Tk()
root.geometry("600x500")
root.configure(bg="#8B008B")
root.title("Казино онлайн без регистрации")

balance = 1000
balance_label = tk.Label(root, text=f"БАЛАНС : {balance}")
balance_label.pack()
balance_label.configure(fg="white", bg="#8B008B", font=("Arial", 20))

bet_label = tk.Label(root, text="Сумма ставки: ")
bet_label.pack()
bet_label.configure(fg = "white", bg='#8B008B', font=("Arial", 20))
bet_entry = tk.Entry(root)
bet_entry.pack()

num_label = tk.Label(root,text="ВВедите число от 1 до 10: ")
num_label.pack()
num_label.configure(fg = "white", bg='#8B008B', font=("Arial", 20))
num_entry = tk.Entry(root)
num_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()
result_label.config(fg = "white", bg='#8B008B', font=("Arial", 20))
def play():
    global balance
    try:
        bet = int(bet_entry.get())
        num = int(num_entry.get())
    except ValueError:
        result_label.config(text="Введите целое число!")
        return

    secret = random.randint(1, 10)

    if bet > balance:
        result_label.config(text="Недостаточно средств, введите ставку заново!")
    elif bet <= 0:
        result_label.config(text="Неверная ставка! ВВедите число больше 0.")
    else:
        if num > 10 or num <= 0:
            result_label.config(text=f"Неверное значение, введите число от 1 до 10!!!")
        elif num == secret:
            result_label.config(text=f"Позравляю вы выиграли: {bet} рублей!")
            balance = balance - bet
            balance = balance + bet * 2
            balance_label.config(text=f"БАЛАНС : {balance}")
        else:
            result_label.config(text=f"Вы просрали {bet} рублей(((")
            balance = balance - bet
            balance_label.config(text=f"БАЛАНС : {balance}")
            if balance <= 0:
                result_label.config(text="Деньги закончились! Игра окончена")
                button.config(state="disabled")
                restart_button.pack()
        bet_entry.delete(0, tk.END)
        num_entry.delete(0, tk.END)
def restart():
    global balance
    balance = 1000
    balance_label.config(text=f"БАЛАНС : {balance}")
    restart_button.pack_forget()
    button.config(state="normal")
    bet_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)
    result_label.config(text="")

def exit_game():
    root.destroy()


button = tk.Button(root, text="Играть", command=play)
button.pack()

restart_button = tk.Button(root, text="Начать заново", command=restart)

exit_button = tk.Button(root, text="Выйти", command=exit_game)
exit_button.place(relx=0.5, rely=0.95, anchor="center")
root.mainloop()
