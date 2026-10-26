#include<stdio.h>
int main(){
    int x=10;
    int*p=&x;
    printf("%d\n",*p);
    *p=50;
    printf("%d\n",*p);
    printf("%p",*p);//wrong
}