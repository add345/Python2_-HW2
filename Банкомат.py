#Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def get_comission(operation: float) -> float:
    result = operation * 0.015

    if result > 600:
        result = 600
    elif result < 30:
        result = 30


    return result

account = 0.0

operation = 0.0

comission = 0

counter = 0

cmd = 0
while cmd != 3:
    if counter % 3 == 0:
        print('Начислены проценты: ', account * 0.03)
        account += account * 0.03

    print(f'Баланс:{account}\nВыберите действие:\nПОПОЛНИТЬ - 1\nСНЯТЬ - 2\nВЫЙТИ - 3')
    cmd = int(input('> '))
    if cmd == 1:
        if account > 5000000:
            account -= account * 0.1

        print('Вы выбрали операцию ПОПОЛНИТЬ')
        operation = float(input('Введите сумму для пополнения: '))

        account += operation

        counter += 1
    elif cmd == 2:
        if account > 5000000:
            account -= account * 0.1

        counter += 1

        print('Вы выбрали операцию СНЯТЬ')
        operation = float(input('Введите сумму для снятия: '))

        comission = get_comission(operation)

        if operation + comission > account:
            print('Сумма и комиссия за снятие наличных превышает баланс! Баланс:', account)
        else:
            account -= operation + comission
            print('Операция снятия успешна! Баланс:', account)
    elif cmd == 3:
        print('Вы выбрали операцию ВЫЙТИ')