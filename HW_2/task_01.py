#Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
# Любое действие выводит сумму денег

deposit_amount = 0
count = 0
SUM_IS_A_MULTIPLE_OF = 50
PERCENT_FOR_WITHDRAWAL = 1.5
MIN_WITHDRAWAL_FEE = 30
MAX_WITHDRAWAL_FEE = 600
PERCENT_ACCRUAL = 3
LIMIT_AMOUNT = 5_000_000
TAX = 10

while True:
    if count % 3 == 0:
        deposit_amount = deposit_amount + deposit_amount * PERCENT_ACCRUAL / 100
        print(f'Сумма вклада {deposit_amount}')
    action = int(input('Выберите действие (1 - пополнить, 2 - снять, 3 - выход): '))
    if deposit_amount > 5_000_000:
        deposit_amount = deposit_amount - deposit_amount * TAX / 100
        print(f'Сумма вклада {deposit_amount}')
    if action == 1:
        sum = int(input('Введите сумму: '))
        if sum % SUM_IS_A_MULTIPLE_OF == 0:
            deposit_amount += sum
            count += 1
            print(f'Сумма вклада {deposit_amount}')
        else:
            print(f'Сумма должна быть кратной {SUM_IS_A_MULTIPLE_OF}')

    if action == 2:
        sum = int(input('Введите сумму: '))
        withdrawai_fee = sum / 100 * PERCENT_FOR_WITHDRAWAL
        if withdrawai_fee <= 30:
            withdrawai_fee = 30
        elif withdrawai_fee >= 600:
            withdrawai_fee = 600
        sum_of = sum + withdrawai_fee
        if sum_of <= deposit_amount:
            if sum % SUM_IS_A_MULTIPLE_OF == 0:
                deposit_amount -= sum_of
                print(f'Сумма вклада {deposit_amount}')
                count += 1
            else:
                print(f'Сумма должна быть кратной {SUM_IS_A_MULTIPLE_OF}')
        else:
            print(f'Недостаточно средств. Сумма вклада {deposit_amount}')
    if action == 3:
        print(f'Сумма вклада {deposit_amount}')
        exit()
