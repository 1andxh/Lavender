pin = "1234"
balance = 1000.00
transaction_history = []

def authenticate():
    attempts = 3
    while attempts > 0:
        input_pin = input("Enter pin (4 digits): ")
        if input_pin == pin:
            print("Authentication successful")
            return True
        else:
            attempts -= 1
            print(f"Wrong pin! Try again. ")
    print("Exceeded limit, Try again later.")
    return False

def check_balance():
    print(f"Current balance: GHS{balance}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print("No negative deposits!")
        else:
            balance += amount
            transaction_history.append(amount)
            print(f"GHS{amount} deposited in your account.")
    except ValueError:
        print("Invalid input")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if balance == 0:
            print("Insufficient funds")
        elif amount > balance:
            print("Insufficient funds to perform action, try again")
        elif amount == balance:
            print("Account can't be empty")
        else:
            balance -= amount
            transaction_history.append(-amount)
            print(f"Withdrawal successful. Available balance: {balance}")
    except ValueError:
        print("Invalid input")

def view_transactions():
    if not transaction_history:
        print("No transactions")
    else:
        print("Your transactions:")
        for transaction in transaction_history:
            print(f" {transaction}")

def menu():
    print("\n=== Menu ===\n1. Check balance\n2. Deposit funds\n3. Withdraw funds\n4. View transaction history\n5. Exit")

def main():
    print("=== Bunk Bank ===")
    
    if not authenticate():
        return
    
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("Thank you for using Bunk Bank.")
            break
        else:
            print("Please choose between options 1-5")

if __name__ == "__main__":
    main()