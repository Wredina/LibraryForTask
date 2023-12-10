
import decimal

MULTIPLICITY = 50
RICHNESS_SUM = 100000
MIN_REMOVAL = 30
MAX_REMOVAL = 600
RICHNESS_PERCENT = 10

balance = decimal.Decimal(0)
operations = []


def check_multiplicity(amount):
    global MULTIPLICITY
    return amount % MULTIPLICITY == 0


def deposit(amount):
    global balance, RICHNESS_SUM, RICHNESS_PERCENT

    if check_multiplicity(amount):
        if amount > RICHNESS_SUM:
            # wealth_tax = Decimal((amount - RICHNESS_SUM) * (RICHNESS_PERCENT / 100))
            # balance += amount - wealth_tax
            balance += amount
            operations.append(
                f'Пополнение на {amount} у.е. Итого {balance} у.е.')
        else:
            balance += amount
            operations.append(
                f'Пополнение карты на {amount} у.е. Итого {balance} у.е.')
    else:
        # commission = MULTIPLICITY * Decimal(15) / Decimal(1000)
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    global balance, MIN_REMOVAL, MAX_REMOVAL
    commission = amount * decimal.Decimal(15) / decimal.Decimal(1000)
    if check_multiplicity(amount):
        commission = amount * decimal.Decimal(15) / decimal.Decimal(1000)
        if commission < MIN_REMOVAL:
            commission = MIN_REMOVAL
        elif commission > MAX_REMOVAL:
            commission = 600
        if balance >= amount + commission:
            balance -= amount + commission
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {commission} у.е.. Итого {balance} у.е.')
        else:
            operations.append(
                f'Недостаточно средств. Сумма с комиссией {amount + commission} у.е. На карте {balance} у.е.')
    else:
        commission = round(
            MULTIPLICITY * decimal.Decimal(15) / decimal.Decimal(1000))
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {MULTIPLICITY + commission} у.е. На карте {balance} у.е.')


def exit():
    global balance, RICHNESS_SUM, RICHNESS_PERCENT
    if balance > RICHNESS_SUM:
        # wealth_tax = balance * (Decimal(RICHNESS_PERCENT) / 100)
        wealth_tax = balance * RICHNESS_PERCENT / 100
        balance -= wealth_tax
        operations.append(
            f'Вычтен налог на богатство 0.1% в сумме {wealth_tax:.4f} у.е. Итого {balance:.4f} у.е.')
        operations.append(f'Возьмите карту на которой {balance:.4f} у.е.')
        return
        # operations.append(f'Возьмите карту на которой {balance} у.е.')
    operations.append(f'Возьмите карту на которой {balance} у.е.')


deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
