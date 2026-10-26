def deposit(bank_accounts):
    acc_no = int(input("Enter account number: "))
    for account in bank_accounts:
        if account[0] == acc_no:
            print("Account found...")
            amount = int(input("enter deposit amount: "))
            if amount <= 0:
                print("invalid amount")
                return
            account[4] += amount
            print(f"Current balance: {int(account[4])}")
            return
    print("Account not found")


def withdraw(bank_accounts):
    acc_no = int(input("Enter account number: "))
    for account in bank_accounts:
        if account[0] == acc_no:
            print("Account found...")
            amount = int(input("Enter withdraw amount: "))
            if amount <= 0:
                print("invalid amount")
                return
            if amount > account[4]:
                print("Insufficient balance")
                return
            account[4] -= amount
            print(f"Current balance: {int(account[4])}")
            return
    print("Account not found")


def show_accounts(bank_accounts):
    print(f"{'Account No':<12} | {'Name':<15} | {'Email ID':<20} | {'Address':<15} | {'Balance':<10}")
    for acc in bank_accounts:
        print(f"{acc[0]:<12} | {acc[1]:<15} | {acc[2]:<20} | {acc[3]:<15} | {acc[4]:<10}")
    


# Main Execution
bank_accounts = []
n = int(input("enter number of customer: "))

for i in range(n):
    print("customer", i + 1)
    account_no = int(input("enter account number: "))
    name = input("enter name: ")
    email_id = input("enter email: ")
    address = input("enter address: ")
    balance = int(input("enter balance: "))

    accounts = [account_no, name, email_id, address, balance]
    bank_accounts.append(accounts)

choice = 0
while choice != 4:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Accounts")
    print("4. Exit")
    choice = int(input("enter choice: "))

    if choice == 1:
        deposit(bank_accounts)
    elif choice == 2:
        withdraw(bank_accounts)
    elif choice == 3:
        show_accounts(bank_accounts)
    elif choice == 4:
        print("thank you")
        break
    else:
        print("invalid choice")