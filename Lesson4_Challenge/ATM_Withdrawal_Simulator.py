# The Smart ATM Withdrawal Simulator 

print("Welcome to the ATM!!")

# Password input
password = int(input("Enter your Password: "))

# A fixed variable bank balance

balance = 500
print(f"Your Balance is:R{balance}")

# Withdrawal money
withdraw = float(input("How much do you want to withdraw?:R").strip())

if withdraw <= balance:
    balance = balance - withdraw
    print(f"Withdrawal Successful! Remaining balance:R({balance})")
elif withdraw <= 0:
    print("Invalid amount.You must withdraw more than R0")
else:
    print("Declined.Insufficient funds")