#include<stdio.h>
int main(){
    int n,sum=0;
    printf("the sum of numbers from 5 to N");
    printf("enter N value : ");
    scanf("%d",&n);
    if(n>5){;
        for(int i=5;i<=n;i++){
            sum+=i;
        }
    } else {
        printf("value is invalid");
    }
    
    printf("the sum of numbers from 5 to %d is %d",n, sum);


    return 0;

}