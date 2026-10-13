num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("the sum is",num1+num2)
print("the diff is",num1-num2)
print("the product is",num1*num2)
print("the exponantion is",num1**num2)
if num2 !=0:
    print("the quotient is",num1/num2)
    print("the floor division is",num1//num2)
    print("the modulus is",num1%num2)
else:
    print("error:division by zero is invalid")