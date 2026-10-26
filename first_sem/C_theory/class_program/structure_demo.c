#include<stdio.h>
#include<string.h>
//structure defination
struct student
{
    //structure member
    int id;
    char name[10];
    char contact[10];
    int pincode;
};
int main()
{
    //creating *structure variable* 'firststudent' of type 'student'
    struct student first_student; 
    struct student second_student; 
    first_student.id=1; //member'id'of 'firststudent' is initialized with 100
    strcpy(first_student.name,"mish"); 
    strcpy(first_student.contact,"8050558195"); 
    first_student.pincode=575001;  
    second_student.id=2;
    strcpy(second_student.name,"aifa");
    strcpy(second_student.contact,"9080544789");
    second_student.pincode=575002;

}
    
