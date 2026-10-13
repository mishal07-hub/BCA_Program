#include<stdio.h>
int main()
{
    int choice,sum, firstnumber,secondnumber;
    printf("----welcome to my calculator-----\n");
    do{
        printf("1 addition\n");
    printf("2 substraction\n");
    printf("3 multiplication\n");
    printf("4 division\n");
    printf("5 exit\n");
    printf("enter my choice");
    scanf("%d", &choice);
    if(choice==1)
    {
    printf("enter first number");
    scanf("%d", &firstnumber);
    printf("enter second number");
    scanf("%d", &secondnumber);
    sum=firstnumber+secondnumber;
    printf("sum of %d", sum);
    }
     if(choice==2)
    {
    printf("enter first number");
    scanf("%d", &firstnumber);
    printf("enter second number");
    scanf("%d", &secondnumber);
    sum=firstnumber-secondnumber;
    printf("sum of %d", sum);
    }
     if(choice==3)
    {
    printf("enter first number");
    scanf("%d", &firstnumber);
    printf("enter second number");
    scanf("%d", &secondnumber);
    sum=firstnumber*secondnumber;
    printf("sum of %d", sum);
    }
     if(choice==4)
    {
    printf("enter first number");
    scanf("%d", &firstnumber);
    printf("enter second number");
    scanf("%d", &secondnumber);
    sum=firstnumber/secondnumber;
    printf("sum of %d", sum);
    }
    if(choice==5)
    {
        printf("the program terminated");
    }
    }
    while(choice!=5);
    return 0;
}
    