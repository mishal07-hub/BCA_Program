#bank operation
#tuple=name,acc_no=1000,pan_no,dob
#list=email,contact,address,balance
n=int(input("enter number of customer:"))
for i in range(n):
    print("customer",i+1)
    name=input("enter name:")
    acc_no=int(input("enter account number:"))
    pan_no=int(input("enter pan number:"))
    dob=int(input("enter DOB:"))
    email=input("enter email:")
    contact=int(input("enter contact no:"))
    address=input("enter address:")
    balance=500
    amount=int(input("enter amount"))
    new_balance=balance+amount
    details=(name,acc_no,pan_no,dob,[email,contact,address,balance])
    balance=details[4][3]
    details[4][3]=new_balance
    print(details)
        