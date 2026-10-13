elements=[]
total=0
for i in range(5):
    element=int(input("enter element:"))
    elements.append(element)
    total=total+elements[i]
print("the sum of list is",total)