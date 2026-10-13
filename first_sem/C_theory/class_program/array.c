// pgm to store and display 5 sub marks
// for student
#include<stdio.h>
int main(){
    int i;
    int sub_marks[5];  //declare an array'sub_mark' with size of 5 of 'int'
    //storing data/array initialization -array_name[index]=data/value;
    sub_marks[0]=80; //stores '80' in array position whose index is '0'
    sub_marks[1]=77;
    sub_marks[2]=74;
    sub_marks[3]=89;
    sub_marks[4]=90; //static array intialization
    printf("sub1 mark:%d\n",sub_marks[0]);
    printf("sub2 mark:%d\n",sub_marks[1]);
    printf("sub3 mark:%d\n",sub_marks[2]);
    printf("sub4 mark:%d\n",sub_marks[3]);
    printf("sub5 mark:%d\n",sub_marks[4]);
    for(int i=0;i<5;i++)
    {
        printf("enter %d subject marks:[int data]",i+1);
        scanf("%d",&sub_marks);
    }
    return 0;
}
