#include<stdio.h>
#include<stdlib.h>
int main(){
    int*p;
    p=(int*)calloc(5,sizeof(int));
    if(p==NULL){
        printf("memory not allocated");
        return 1;
    }
    for(int i=0;i<6;i++){
        printf("location %d:address= %p,value=%d\n",i,(int *)(p+i),*(p+i));
    }
    free(p);
    return 0;

    

}