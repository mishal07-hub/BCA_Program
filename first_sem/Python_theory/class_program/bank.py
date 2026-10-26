#bank operation
#tuple=name,acc_no=1000,pan_no,dob
#list=email,contact,address,balance
n=int(input("enter number of customer:"))
acc_detail=[]
for i in range(n):
    print("customer",i+1)
    name=input("enter name:")
    acc_no=int(input("enter account number:"))
    pan_no=int(input("enter pan number:"))
    dob=int(input("enter DOB:"))
    email=input("enter email:")
    contact=int(input("enter contact no:"))
    address=input("enter address:")
    balance=int(input("enter balance:"))
    details=(name,acc_no,pan_no,dob,[email,contact,address,balance])
    acc_detail.append(details)
    choice=0
while choice!=4:
    print("1.deposit")
    print("2.wthdraw")
    print("3.display")
    print("4.exit")
    choice=int(input("enter choice"))
    if choice in(1,2,3):
        search=int(input("enter account no"))
        for i in range(len(acc_detail)):
            if acc_detail[i][1]==search:
                if choice==1:
                    amount=int(input("enter amount"))
                    balance=acc_detail[i][4][3]
                    new_balance=balance+amount
                    acc_detail[i][4][3]=new_balance
                    print("balance is %d",new_balance)   
                elif choice==2:
                    amount=int(input("enter amount"))
                    balance=acc_detail[i][4][3]
                    if balance>=amount:
                        new_balance=balance-amount
                        acc_detail[i][4][3]=new_balance
                        print("balance is",new_balance)
                    else:
                        print("insufficent balance")
                elif choice==3:
                    print("name:",acc_detail[i][0])
                    print("account no:",acc_detail[i][1])
                    print("balance",acc_detail[i][4][3])
                elif choice==4:
                    print("thank you")
                    break
                else:
                    print("invalid  choice")          
print(acc_detail)