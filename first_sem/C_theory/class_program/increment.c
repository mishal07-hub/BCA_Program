#include<stdio.h>
int main(){
    int a=100;
    int*p=&a;
    int m=*p++;
    int n=++*p;
    printf("%d\n",m);
    printf("%d\n",n);
} 