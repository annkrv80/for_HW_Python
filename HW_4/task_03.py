#Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
#Дополнительно сохраняйте все операции поступления и снятия средств в список.

from decimal import *

deposit_amount = 0
count = 1
flag = True
SUM_IS_A_MULTIPLE_OF = 50
PERCENT_FOR_WITHDRAWAL = 1.5
MIN_WITHDRAWAL_FEE = 30
MAX_WITHDRAWAL_FEE = 600
PERCENT_ACCRUAL = 3
LIMIT_AMOUNT = 5_000_000
TAX = 10


def depositing_money(deposit):
    sum = int(input('Введите сумму: '))
    if sum % SUM_IS_A_MULTIPLE_OF == 0:
        deposit += sum
        global count
        count += 1
        print(f'Сумма вклада {deposit}')
        operations_information_write(f'Replenishment in the {sum} rub\n')
        return deposit  
    else:
        print(f'Сумма должна быть кратной {SUM_IS_A_MULTIPLE_OF}')
        return deposit


def removal_of_money(deposit):
    sum = int(input('Введите сумму: '))
    withdrawai_fee = Decimal(sum / 100 * PERCENT_FOR_WITHDRAWAL)
    if withdrawai_fee <= 30:
        withdrawai_fee = 30
    elif withdrawai_fee >= 600:
        withdrawai_fee = 600
    sum_of = sum + withdrawai_fee
    if sum_of <= deposit:
        if sum % SUM_IS_A_MULTIPLE_OF == 0:
            deposit -= sum_of
            global count
            count += 1
            print(f'Сумма вклада {deposit}')
            operations_information_write(f'Withdrawal amount the {sum} RUB and commission\
    {withdrawai_fee} RUB \n')
            return deposit
        else:
            print(f'Сумма должна быть кратной {SUM_IS_A_MULTIPLE_OF}')
            return deposit
    else:
        print(f'Недостаточно средств. Сумма вклада {deposit}')
        return deposit


def accrual_of_interest(deposit):
    deposit = Decimal(deposit + deposit * PERCENT_ACCRUAL / 100)
    operations_information_write(f'Accrued interest {deposit * PERCENT_ACCRUAL / 100} rub\n')
    return deposit


def payment_of_taxes(deposit):
    deposit = Decimal(deposit - deposit * TAX / 100)
    operations_information_write(f'Payment of tax {deposit * TAX / 100} rub\n')
    print(f'Сумма вклада {deposit}')
    return deposit


def account_information_write(deposit):
    with open('deposit.txt', 'w') as f:
        f.write(str(deposit))


def operations_information_write(info):
    with open('operation.txt', 'a') as f:
        f.write(str(info))


with open('deposit.txt', 'r') as f:
    deposit_amount = Decimal(f.read())
    print(f'Ваш баланс {deposit_amount}')


while flag:
    if count % 3 == 0:
        deposit_amount = accrual_of_interest(deposit_amount)    
    action = int(input('Выберите действие (1 - пополнить, 2 - снять, 3 - выход): '))
    if deposit_amount > 5_000_000:
        deposit_amount = payment_of_taxes(deposit_amount)
    if action == 1:
        deposit_amount = depositing_money(deposit_amount)     
    if action == 2:
        deposit_amount = removal_of_money(deposit_amount)        
    if action == 3:
        print(f'Сумма вклада {deposit_amount}')
        account_information_write(deposit_amount)
        flag = False
        