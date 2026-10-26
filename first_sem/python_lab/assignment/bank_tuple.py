n=int(input("enter number of customer:"))
acc_detail=[]
for i in range(n):
    print("customer",i+1)
    account_no=int(input("enter account number:"))
    name=input("enter name:")
    dob=int(input("enter DOB:"))
    email_id=input("enter email:")
    contact_no=int(input("enter contact no:"))
    address=input("enter address:")
    balance=int(input("enter balance:"))
    details=(account_no,name, dob, [email_id, contact_no,address, balance])
    acc_detail.append(details)
    print("1.deposit")
    print("2.display")
    choice=("enetr choice:")
    if choice==1:
        amount=int(input("enter amount"))
        balance=acc_detail[i][3][3]
        new_balance=balance+amount
        acc_detail[i][3][3]=new_balance
        print("balance is %d",new_balance)
    else:
        print(f"{'account_no':<15}{'name':<15}{'dob':<10}{'email':<10}{'contact':<10}{'balance':<10}")
        print(f"{details[0]:<15}{details[1]:<15}{details[2]:<10}{details[3]:<10}{details[4]:<10}{details[5]:<10}")   
print("\n---demonstrating tuple immutablility-------")
try:
    print("attempting to modify tuple element")
    details[0]=10001
except TypeError as e:
    print("error caught:",e)


               
