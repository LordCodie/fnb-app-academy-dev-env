bank_balance = 500.00

withdrawal_amount = float(input("Enter amount you wish to withdraw: "))


if withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0")
elif withdrawal_amount < bank_balance: 
    print(f"Withdrawal successful! Remaining balance: R{bank_balance - withdrawal_amount}")
else:
    print("Declined. Insufficient funds")

