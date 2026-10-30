#include<stdio.h>
int push(int stack[],int newdata,int size,int top){
    if(top==size-1){
        printf("stack overflow\n");
    }
    else{
        top++;
        stack[top]=newdata;
        printf("number entered succesfully\n");
    }
    return top;
    }
int pop(int stack[],int top){
    if(top==-1){
        printf("stack underflow\n");
    }
    else{
        printf("deleted element:%d\n",stack[top]);
        top--;
    }
    return top;
}
void display(int stack[],int top){
    if(top==-1){
        printf("stack is empty\n");
    }
    else{
        printf("stack element are:\n");
        for(int i=top;i>=0;i--){
            printf("%d\n",stack[i]);
        }
    }
}
int main(){
    int size=5;
    //declare one stack to hold 5 integer data
    int stack[size];
    int top=-1;//to represent stack top.intially contain -1
    int choice,number;
    do
    {
        printf("1.push data\n");
        printf("2.pop data\n");
        printf("3.display stack\n");
        printf("4.exit\n");
        printf("enter choice:");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
        printf("enter stack number");
        scanf("%d",&number);
        top=push(stack,number,size,top);
        break;
        case 2:
        printf("enter stack number");
        scanf("%d",&number);
        top=pop(stack,top);
        break;
        case 3:
        display(stack,top);
        break;
        case 4:
        printf("exit");
        break;
        default:
        printf("invalid choice");
            break;
        }
        
    } while (choice<4);
    return 0;


    
}