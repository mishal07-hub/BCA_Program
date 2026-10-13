#include <stdio.h>
int get_array_sum(int number[]){
    int i,total=0;
    for(i=0;i<5;i++)
    {
        total=total+number[i];
        printf("total is:%d\n",total);
    }
    return total;
}
int main(){
    int mynumber[5];
    for(int i=0;i<5;i++){
        printf("number %d is\n",i+1);
        scanf("%d",&mynumber[i]);
    }
    int sum=get_array_sum(mynumber);
    printf("the sum is %d",sum);
        
}