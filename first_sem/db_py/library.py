import mysql.connector
#database connection

def connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mishal123",
        database="librarydb"
    )
    return con


def add_student_detail(con):
    cursor=con.cursor()
    student_id=input("enter student id:")
    student_name=input("enter student name:")
    age=int(input("enter age:"))
    email=input("enter email:")
    phone=int(input("enter phone:"))
    query="insert into student(student_id,student_name,age,email,phone)values(%s,%s,%s,%s,%s)"
    values=(student_id,student_name,age,email,phone)
    cursor.execute(query,values)
    con.commit()
    print("student details added successfully")


    #con=connection()   
    #add_student_detail(con)
#add book detail fuction

#add issue detail fuction
#display issue detail function



    #get student data
#cursor=con.cursor()
#cursor.execute("select * from student")
#record=cursor.fetchall()
def add_book_detail(con):
     
    cursor=con.cursor()

    book_id=input("enter book id:")
    book_name=input("enter book name:")
    author=input("enter author:")
    category=input("enter category:")
    no_of_pg=int(input("enter no of pg:"))

    query="insert into book(book_id,book_name,author,category,no_of_pg)values(%s,%s,%s,%s,%s)"

    values=(book_id,book_name,author,category,no_of_pg)

    cursor.execute(query,values)
    con.commit()
    print("book details added successfully")

def add_issue(con):
    cursor=con.cursor()

    student_id=input("enter student id:")
    book_id=input("enter book id:")
    issue_date=int(input("enter issue date(yyyy-mm-dd):"))
    return_date=int(input("enter return dare(yyyy-mm-dd):"))

    query="insert into issue(student_id,book_id,issue_date,return_date)values(%s,%s,%s,%s)"
    values=(student_id,book_id,issue_date,return_date)

    cursor.execute(query,values)
    con.commit()
    print("issue details added successfully")

def display_issue(con):
    cursor=con.cursor()
    query="""select i.issue_id,s.student_name ,b.book_name,i.issue_date,i.return_date from issue i 
    join student s on s.student_id=i.student_id
    join book b on b.book_id=i.book_id """

    cursor.execute(query)

    records=cursor.fetchall()

    for record in records:
        print(record)
con=connection()  
if con.is_connected():
    print("connection established successfully")


while True:
    print("-------library managment system-------")
    print("1.adding student detail")
    print("2.adding book detail")
    print("3.adding issue detail")
    print("4.display issue detail")
    print("5.exit")
    choice=input("enter your choice")
    if choice==1:
        add_student_detail(con) 
    elif choice==2:
        add_book_detail(con)
    elif choice==3:
        add_issue(con)
    elif choice==4:
        display_issue(con)
    elif choice==5:
        con.close()
        print("application close")
    else:
        print("invalid choice")
