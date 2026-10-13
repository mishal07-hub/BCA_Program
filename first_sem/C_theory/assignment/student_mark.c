#include<stdio.h>
void details(char name[][50],int roll[],int marks[][5]){
    for(int i=0;i<5;i++){
        printf("student%d\n",i+1);
        printf("enter student name:");
        scanf("%s",name[i]);
        printf("enter roll number:");
        scanf("%d",&roll[i]);
        for(int j=0;j<5;j++){
            printf("sub%d\n",j+1);
            printf("enter marks:");
            scanf("%d",&marks[i][j]);
        }
        printf("\n");
    }
}
int calculatetotal(int marks[]){
    int total=0;
    for(int j=0;j<5;j++){
        total=total+marks[j];
    }
    return total;
}
int checkpass(int marks[])
{
    int j;
    for(j=0;j<5;j++){
        if(marks[j]<35){
            return 0;
        }
    }
    return 1;
}
void displayresult(char name[][50],int roll[],int marks[][5]){
    int i,total,pass;
    float average,percentage;
    char *result;
    
    printf("----------------------------------------------------------------------------------------------------------------------------------------------------\n");
    printf("| %-10s | %-15s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s |\n",
        "roll_no","name","python","computer","english","math","DBMS","total","average","percentage","result");
        printf("---------------------------------------------------------------------------------------------------------------------------------------------------\n");
        for(i=0;i<5;i++){
        total=calculatetotal(marks[i]);
        average=total/5.0f;
        percentage=(total/500.0f)*100.0f;
        pass=checkpass(marks[i]);
        if(pass==1){
            result="pass";
        }
        else{
            result="fail";
        }
        printf("| %-10d | %-15s | %-10d | %-10d | %-10d | %-10d | %-10d | %-10d | %-10.2f | %-10.2f | %-10s |\n",
            roll[i],name[i],marks[i][0],marks[i][1],marks[i][2],marks[i][3],marks[i][4],total,average,percentage,result);
        
    }
}
int main(){
    int roll[5];
    char name[5][50];
    int marks[5][5];
    details(name,roll,marks);
    displayresult(name,roll,marks);
    return 0;
}