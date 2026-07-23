print("===== TASK 1: The Cash Dispenser =====")

def count_notes(amount, note_value):
    return amount // note_value

withdraw_amount = int(input("Enter amount to withdraw: "))

if withdraw_amount % 50 != 0:
    print("The machine only dispenses multiples of 50 EGP.")
elif withdraw_amount > 10000:
    print("Daily limit is 10000 EGP.")
else:
    remaining_amount = withdraw_amount

    notes_500 = count_notes(remaining_amount, 500)
    remaining_amount = remaining_amount % 500

    notes_200 = count_notes(remaining_amount, 200)
    remaining_amount = remaining_amount % 200

    notes_100 = count_notes(remaining_amount, 100)
    remaining_amount = remaining_amount % 100

    notes_50 = count_notes(remaining_amount, 50)
    remaining_amount = remaining_amount % 50

    if notes_500 > 0:
        print("500 x", notes_500)
    if notes_200 > 0:
        print("200 x", notes_200)
    if notes_100 > 0:
        print("100 x", notes_100)
    if notes_50 > 0:
        print("50 x", notes_50)

    total_notes = notes_500 + notes_200 + notes_100 + notes_50
    print("Total notes:", total_notes)


print("\n===== TASK 2: The Savings Goal =====")

def grow(balance, monthly):
    balance = balance + monthly
    balance = balance * 1.012
    return balance

opening_balance = float(input("Enter opening balance: "))
monthly_deposit = float(input("Enter monthly deposit: "))
savings_goal = float(input("Enter savings goal: "))

balance = opening_balance
months = 0
total_deposited = 0

while balance < savings_goal and months < 120:
    balance = grow(balance, monthly_deposit)
    months = months + 1
    total_deposited = total_deposited + monthly_deposit
    print(f"Month {months}: {balance:.2f} EGP")

if balance >= savings_goal:
    interest_earned = balance - opening_balance - total_deposited
    print(f"Reached the goal in {months} months")
    print(f"Total deposited: {total_deposited:.2f} EGP")
    print(f"Interest earned: {interest_earned:.2f} EGP")
else:
    print("Goal not reachable in 10 years.")


print("\n===== TASK 3: Is This Card Real? =====")

def get_luhn_total(card_number):
    total = 0
    position = 1
    while card_number > 0:
        digit = card_number % 10
        if position % 2 == 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total = total + digit
        card_number = card_number // 10
        position = position + 1
    return total

def is_valid_card(card_number):
    return get_luhn_total(card_number) % 10 == 0

card_number = int(input("Enter card number: "))

if is_valid_card(card_number):
    print("VALID card number")
else:
    print("INVALID card number")
