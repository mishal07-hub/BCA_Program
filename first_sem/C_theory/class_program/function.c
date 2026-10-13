#include<stdio.h>
int roll_number;
float sub1,sub2,sub3,sub4,sub5,total,average,cgpa;
void get_student_data(){
    printf("enter roll number:");
    scanf("%d",&roll_number);
    printf("enter english marks:");
    scanf("%f",&sub1);
    printf("enter math marks:");
    scanf("%f",&sub2);
    printf("enter computer marks:");
    scanf("%f",&sub3);
    printf("enter dbms marks:");
    scanf("%f",&sub4);
    printf("enter python marks:");
    scanf("%f",&sub5);

}
void mark_total(){
    total=sub1+sub2+sub3+sub4+sub5;
    printf("total=%.2f\n",total);
}
float mark_average(){
    average=total/5;
    printf("average is %.2f\n",average);
    return average;       //return 'average'to main()
}
void mark_cgpa(){
    cgpa=average/9.5;
    printf("cgpa:%.2f\n",cgpa);
}
int main()
{
    get_student_data();
    mark_total();
    mark_average();
    mark_cgpa();
}

    
    
