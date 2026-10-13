#include<stdio.h>
int main(){
    int i,j;
    for(j=0;j<=5;j++){
        printf("loop started\n");
        for(i=0;i<5;i++){
            printf("inner loop started\n");
            break;
            printf("from inner loop\n");
        }
        printf("from outer loop\n");
        break;
    }
    printf("program terminated..");
    return 0;
}