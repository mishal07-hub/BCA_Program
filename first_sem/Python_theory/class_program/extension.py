#process a single student data, data are as followed:
#name,roll_no,phone,email,5 sub marks and get sub total
#implimented by using nested list
def student_detail():
    name=input("name:")
    roll_no=int(input("roll no:"))
    phone=int(input("phone number:"))
    email=input("email:")
    return name,roll_no,phone,email
def marks():
    sub=[]
    for i in range(5):
        mark=int(input(" sub marks " + str(i+1) + ":"))
        sub.append(mark)
        return [sub]
def total_mark():
    global total
    for i in range(len(sub)):
        total=0
        total+=sub[i]
        print("total is",total)
        return total
for i in range(1):
    [name,roll_no,phone,email,[sub]]=student_detail
    sub=marks
    total=total_mark
    