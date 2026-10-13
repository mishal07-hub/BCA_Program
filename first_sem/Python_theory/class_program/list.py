marks=['raj',95,88,78,68,87] #declares an list with name 'marks' to store marksof 'sachin'-static
my_mark=[]#dynamic intialization
sum=0
for i in range(5):
    mark=int(input("enter the marks:"))
    my_mark.append(mark)
print("list element are:")
for i in range(len(my_mark)):
    print(i+1,"mark is",my_mark[i])
for i in range(len(my_mark)):
    sum+=my_mark[i]
print("total is",sum)