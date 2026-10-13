#bank operation
#tuple=name,acc_no=1000,pan_no,dob
#list=email,contact,address,balance
name=input("enter name:")
acc_no=int(input("enter account number:"))
pan_no=int(input("enter pan number:"))
dob=int(input("enter DOB:"))
email=input("enter email:")
contact=int(input("enter contact no:"))
address=input("enter address:")
balance=500
print("1.deposit" \
    "2.wthdraw" \
    "3.display" \
    "4.exit")
choice=int(input("enter choice"))
if choice==1:
    amount=int(input("enter amount"))
    balance=balance+amount
    print("balance is%d",balance)
    
elif choice==2:
    amount=int(input("enter amount"))
    balance=balance-amount
    print("balance is",balance)
    

elif choice==3:
    print(name)
    print(acc_no)
    print(balance)
else:
    print("thank you")

details=((name,acc_no,pan_no,dob),[email,contact,address,balance])
print(details)

