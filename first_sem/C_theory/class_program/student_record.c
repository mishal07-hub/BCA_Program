#include<stdio.h>
#include<string.h>
//global array of structure 'students' with size 5
//can be accessed in every function
struct student_record
{
    char name[50];
    int roll_no;
    int marks[3];
    int total;
    float average;
    float percentage;
};
struct student_record student[5];

//method to initialize 5 students
void intialize_student(){
    struct student_record student[5];
    int i,j;
    for(i=0;i<5;i++)
    {
        printf("student %d",i+1);
        printf("name:");
        scanf("%s",&student[i].name);
        printf("roll_no:");
        scanf("%d",&student[i].roll_no);
        //to collect 3 sub marks
        for (int j = 0; j<3; j++)
        {
            printf(" marks of subject %d:",j+1);
            scanf("%d",&student[i].marks[j]);
        }
    }
    
}
int calculate_total(int marks[]){
    int j;
    int sum=0;
    for(j=1;j<=3;j++){
        sum=sum+marks[j];
        
    }
    return sum;
}
float calculate_average(float total ){
    return(total/3);
}
float calculate_percentage(float total){
    return(total/300)*100;
}
void display_student(){
    int i;
    for(i=0;i<5;i++){
        printf("\n----student detail----");
        printf("roll_no:%d\n",student[i].roll_no);
        printf("name:%s\n",student[i].name);
        printf("phython marks:%d\n",student[i].marks[0]);
        printf("english marks:%d\n",student[i].marks[1]);
        printf("math marks:%d\n",student[i].marks[2]);
        printf("total=%d\n",student[i].total);
        printf("average=%.2f\n",student[i].average);
        printf("percentage=%.2f\n",student[i].percentage);
    }
}

int main(){
    struct student_record student[5];
    intialize_student();

    for(int i=0;i<5;i++){
        student[i].total=calculate_total(student[i].marks);
        student[i].average=calculate_average(student[i].total);
        student[i].percentage=calculate_percentage(student[i].total);
    }
    display_student();

    return 0;
    }


