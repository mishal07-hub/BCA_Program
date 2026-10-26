#include<stdio.h>
#include<string.h>
struct software
{
    int id;
    char name[50];
    float salary;
    char email[50];
    char phone[10];
};
int main()
{    
    struct software first_emp;
    struct software second_emp;
    first_emp.id=101;
    strcpy(first_emp.name,"kim");
    first_emp.salary=85000;
    strcpy(first_emp.email,"kim@gmail.com");
    strcpy(first_emp.phone,"94856778549");
    second_emp.id=102;
    strcpy(second_emp.name,"raj");
    second_emp.salary=80000;
    strcpy(second_emp.email,"raj@gmail.com");
    strcpy(second_emp.phone,"9485672547");

}