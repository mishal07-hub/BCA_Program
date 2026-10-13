#include<stdio.h>
int main(){
    int choice=2;
    int accountno=2580;
    float amount;
    float balance=500;
    int useraccount,deposit_amount,withdraw_amount,display_amount;
    printf("---welcome to my bank---");
    printf("1 deposit");
    printf("2 withdraw");
    printf("3 account_view");
    printf("4 exit");
    printf("enter my choice");
    scanf("%d",&choice);
    switch (choice)
    {
    case 1:
        printf("enter account no");
        scanf("%d",&useraccount);
        if(useraccount=accountno)
        {
        printf("enter deposit amount");
        scanf("%d",&deposit_amount);
        balance=balance+deposit_amount;
        }
        else{
            printf ("accountno is invalid");
        }
        break;
    case 2:
        printf("enter account no");
        scanf("%d",&useraccount);
        if(useraccount=accountno)
        {
        printf("enter withdraw amount");
        scanf("%d",withdraw_amount);
        balance=balance-withdraw_amount;
    }
        else{
            printf("accountno is invalid");
        }
        break;
    case 3:
        printf("enter account no");
        scanf("%d",&useraccount);
        if(useraccount=accountno)
        {
            printf("your balance is:%d",balance);
        }
        else{
            printf("accountno is in valid");
        }
        break;
    case 4:
        printf("exit");
        break;
    default:
        printf("invalid choice");
        break;
    }
}