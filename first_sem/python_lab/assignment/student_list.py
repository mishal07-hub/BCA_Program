def read_student_detail():
    students_marks=[]
    for i in range(5):
        print("student",i+1)
        name=input("enter name:")
        python=int(input("enter python marks:"))
        computer=int(input("enter computer marks: "))
        math=int(input("enter math marks:"))
        english=int(input("enter english marks:"))
        dbms=int(input("enter dbms marks:"))
        student=[name,python,computer,math,english,dbms]
        students_marks.append(student)
    return students_marks
def calculate_total(students_marks):
    for student in students_marks:
        total=sum(student[1:])
        student.append(total)
def display_students(students_marks):
    print(f"{'name':<15}{'python':<10}{'computer':<10}{'math':<10}{'english':<10}{'dbms':<10}{'total':<10}")
    for student in students_marks:
        name=student[0]
        python,computer,math,english,dbms=student[1:6]
        total=student[6]
        print(f"{name:<15}{python:<10}{computer:<10}{math:<10}{english:<10}{dbms:<10}{total:<10}")

students_marks=read_student_detail()
calculate_total(students_marks)
display_students(students_marks)
        