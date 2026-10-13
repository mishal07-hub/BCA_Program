#include<stdio.h>
int main(){
    int roll_no,python,computer,math,english,dbms;
    float total,average,percentage;
    printf("enter roll_no:");
    scanf("%d",&roll_no);
    printf("enter python marks:");
    scanf("%d",&python);
    printf("enter computer marks:");
    scanf("%d",&computer);
    printf("enter math marks:");
    scanf("%d",&math);
    printf("enter english marks:");
    scanf("%d",&english);
    printf("enter DBMS marks:");
    scanf("%d",&dbms);
    total=python+computer+math+english+dbms;
    average=total/5;
    percentage=(total/500)*100;
    printf("----------student result-----------\n");
    printf("roll_no:%d\n",roll_no);
    printf("python marks:%d\n",python);
    printf("computer marks:%d\n",computer);
    printf("math marks:%d\n",math);
    printf("english marks:%d\n",english);
    printf("DBMS marks:%d\n",dbms);
    printf("total marks:%.2f\n",total);
    printf("average:%.2f\n",average);
    printf("percentage:%.2f\n",percentage);

    
}