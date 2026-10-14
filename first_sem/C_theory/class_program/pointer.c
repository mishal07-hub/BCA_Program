#include<stdio.h>
int main(){
    int x=8; //variable which stores 10
    int*p;    //intializing pointer
    p=&x;       //intializing pointer to x to store address of x
    printf("%d\n",x);
    printf("%p\n",&x);
    printf("%p",p);
}