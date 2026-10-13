balance=500
account_no=int(input("enter account number:"))
while True:
    print("-------bank menu-------")
    print("1.deposit")
    print("2.withdraw")
    print("3.account details")
    print("4.exit")
    choice=input("enter choice:")
    if choice=="1":
        deposit=float(input("enter deposit amount:"))
        if deposit<=0:
            print("invalid amount")
        else:
            balance=balance+deposit
            print(f"deposited {deposit:.2f}")
            print("total balance is:",round(balance,2))
    elif choice=="2":
        withdraw=float(input("enter withdraw amount:"))
        if withdraw<=0:
            print("invalid amount")
        elif withdraw>balance:
            print("insufficient balance")
        else:
            balance=balance-withdraw
            print(f"withdraw {withdraw:.2f}")
            print("total balance is:",round(balance,2))
    elif choice=="3":
        print(f"account number:{account_no}")
        print(f"total balance:{balance}")
    elif choice=="4":
        print("exit")
        break
    else:
        print("invalid choice")

    

