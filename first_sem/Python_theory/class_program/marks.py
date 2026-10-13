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
def total_marks():
    global total
    total=python+math+dbms
    print("total:",total)
def get_average():
    average=total/3
    print("averag:",average)
def get_percentage():
    global percentage
    percentage=total/300*100
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
read_data()
total_marks()
get_average()
get_percentage()
find_grade()
                    
                        

                    
                
                
    


    
