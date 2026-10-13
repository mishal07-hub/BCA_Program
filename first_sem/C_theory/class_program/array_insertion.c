#include<stdio.h>
int main()
{
    int i,new_element,index_number;
    int element[5];
    for(i=0;i<4;i++)
    {
        printf("element %d:",i+1);
        scanf("%d",&element[i]);
    }
    printf("enter new element:");
    scanf("%d",&new_element);
    printf("enter index number");
    scanf("%d",&index_number);
    //insertion process to insert 'new_element' at index'index'
    element[4]=element[3];
    element[3]=element[2];
    element[2]=new_element;
    //printing update
    for(int i=0;i<5;i++)
    {
        printf(" %d ",element[i]);
    }
}