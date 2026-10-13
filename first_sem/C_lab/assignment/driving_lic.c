#include<stdio.h>
int main(){
    int age;
    char nationality,result,fee;
    printf("are you indian?(y/n):");
    scanf(" %c",&nationality);
    
    if(nationality=='y'){
        printf("enter age:");
        scanf("%d",&age);
        if(age>=18)
        {
            printf("test passed?(y/n):");
            scanf(" %c",&result);
            if(result=='y'){
                printf("fee paid?(y/n):");
                scanf(" %c",&fee);
                if(fee=='y'){
                    printf("congragulation you are eligible for DL");
                }
                else{
                    printf("reason for failure:fee not paid");
                }
            }
            else
            {
                printf("reason for failure:failed test");
            }

        }
        else{
            printf("reason for failure:age should be >=18");
        }

    }
    else{
        printf("reason for failure:should be an Indian");
    }
    return 0;
}
    
    