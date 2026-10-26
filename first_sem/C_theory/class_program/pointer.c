#include<stdio.h>
int main(){
    //pointer which stores address of another variable
    int x=8; //variable which stores 8
    int*p;    //declaring pointer
    p=&x;       //intializing pointer to x to store address of x,& address operator
    printf("%d\n",x);
    printf("%p\n",&x);//address of x
    printf("%p",p);
}