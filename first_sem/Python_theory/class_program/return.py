name=''
roll_no=0
python=0
math=0
dbms=0
total=0
percentage=0
def read_data():
    global math,python,dbms
    name=input("enter name:")
    roll_no=int(input("roll number:"))
    python=int(input("python marks:"))
    math=int(input("math marks:"))
    dbms=int(input("dbms marks:"))
    return name,roll_no,python,math,dbms
def total_marks():
    global total
    total=python+math+dbms
    print("total:",total)
def get_average():
    average=total/3
    return total
    print("averag:",average)
def get_percentage():
    global percentage
    percentage=total/300*100
    return percentage
    print("percentage:",percentage)
def find_grade():
    if percentage>=75:
        print("distinction")
    elif percentage>=60:
        print("firstclass")
    elif percentage>40:
        print("second class")
    else:
        print("fail")
for i in range(1,4):
    a,b,c,d,e=read_data()
    total=total_marks()
    average=get_average()
    percentage=get_percentage()
    find_grade()