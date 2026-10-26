#collect emp_name,emp_no,comp_name,salary
emp_name=input("enter emp name:")
emp_no=int(input("enter emp number:"))
comp_name=input("enter company name:")
salary=float(input("enter salary:"))
contact=int(input("enter contact number:"))
dept=input("enter dept:")
dict={
    "name":emp_name,
    "emp number":emp_no,
    "company name":comp_name,
    "salary":salary,
}
set={emp_name,emp_no,comp_name,salary}
set.update({contact,dept})
dict.update({"contact":contact,"dept":dept})
print("dictionary",dict)
print("set",set)

print("="*90)
print(f"{'name':<15}|{'emp_no':<15}|{'company_name':<15}|{'salary':<15}|{'contact':<15}|{'dept':<10}")
print(f"{emp_name:<15}|{emp_no:<15}|{comp_name:<15}|{salary:<15}|{contact:<15}|{dept:<10}")
print("="*90)

print("\ndictionary")
print(f"{'key':<12}|{'value'}")
print("-"*25)
for key, value in dict.items():
    print(f"{key:<12}|{value}")

print("\nset:")
print(f"{'value'}")
print("-"*15)
for item in set:
    print(item)