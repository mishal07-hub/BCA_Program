all_account=[]

account_no=int(input("enter account number:"))
name=input("enter name:")
dob=int(input("enter DOB:"))
email=input("enter email:")
contact=int(input("enter contact no:"))
address=input("enter address:")
balance=500
amount=int(input("enter amount:"))
new_balance=balance+amount

details=(account_no,name,dob,[email,contact,address,balance])
all_account.append(details)

balance=details[3][3]
details[3][3]=new_balance
print(f"{'account_no':<15}|{'name':<15}|{'dob':<10}|{'email':<20}|{'contact':<10}|{'balance':<10}")
print(f"{details[0]:<15}|{details[1]:<15}|{details[2]:<10}|{details[3][0]:<20}|{details[3][1]:<10}|{details[3][3]:<10}")   

print("\n---demonstrating tuple immutablility-------")
try:
    print("attempting to modify tuple element")
    details[0]=10001
except TypeError as e:
    print("error caught:",e)