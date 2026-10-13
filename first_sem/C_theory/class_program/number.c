#include<stdio.h>
int main(){
    int i,j;
    for(i=1;i<=5;i++){
        for(j=1;j<=i;j++){
            printf("%d ",j);
        }
        printf("\n");
        
    }
    
    int;
    for(i=5;i>=1;i--){
        for(j=1;j<=i;j++){
            printf("%d ",j);
        }
        printf("\n");
        
    }
    for(i=5;i>=1;i--){
        for(j=1;j<=i;j++){
            if(i==5){
                if(j==3){
                    printf("_ ");
                }else{
                    printf("%d ",j);
                }
            }
             else{
                printf("%d ",j);
            }
            
        }    
        printf("\n");   
        
    }
    return 0;
}
   