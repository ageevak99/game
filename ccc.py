balance = 1000
print(f"Добрый день! Ваш баланс {balance}")
while balance > 0:
    bet = int(input("Введите сумму ставки: "))
    if balance >= bet:
        balance = balance - bet
        num = int(input("Выберите число от 1 до 10: "))
        while num > 10 or num < 1:
            num = int(input("Выберите число от 1 до 10: "))
        import random
        secret = random.randint(1, 10)
        if num == secret:
            print(f"Позравляю вы выиграли: {bet} рублей!")
            balance = balance + bet*2
        else:
            print(f"Вы просрали {bet} рублей(((")
    else:
        print('Недостаточно средств, введите ставку заново.')
    print(f"Ваш баланс: {balance}")
    if balance <= 0:
        print("Поздравляю! Вы просрали всё!")
        break
    answer = input("Продолжим игру? (да/нет) ")
    if answer == "нет":
        break