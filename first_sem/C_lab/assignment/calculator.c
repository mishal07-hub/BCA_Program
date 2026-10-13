#include<stdio.h>
int main(){
    int choice,addition,substraction,multiplicaltion,modulus,a,b;
    float division,num1,num2;
    printf("---choose your operation---\n");
    printf("1. addition\n");
    printf("2.substraction\n");
    printf("3.multiplication\n");
    printf("4.divison\n");
    printf("5.modulus\n");
    printf("enter choice:");
    scanf("%d",&choice);
    switch (choice)
    {
    case 1:
        printf("enter number:");
        scanf("%d",&a);
        printf("enter number:");
        scanf("%d",&b);
        printf("sum=%d",a+b);
        break;
    case 2:
        printf("enter number:");
        scanf("%d",&a);
        printf("enter number:");
        scanf("%d",&b);
        printf("diff=%d",a-b);
        break;
    case 3:
        printf("enter number:");
        scanf("%d",&a);
        printf("enter number:");
        scanf("%d",&b);
        printf("product=%d",a*b);
        break;
    case 4:
    printf("enter number:");
        scanf("%f",&num1);
        printf("enter number:");
        scanf("%f",&num2);
        printf("quotient=%.2f",num1/num2);
        break;
    case 5:
        printf("enter number:");
        scanf("%d",&a);
        printf("enter number:");
        scanf("%d",&b);
        printf("modulus=%d",a%b);
        break;
    default:
        printf("invalid choice");
        break;
    }

}