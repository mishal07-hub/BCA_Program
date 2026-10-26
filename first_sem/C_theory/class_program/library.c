#include<stdio.h>
#include<string.h>
struct library
{
    int library_id;
    char book_name[10];
    char author_name[10];
    char genre[10];
    int pg_no;
};
int main(){
    struct library firstmember;
    struct library seondmember;
    struct library thirdmember;
    struct library fourthmember;
    struct library fifthmember;
    firstmember.library_id=101;
    strcpy(firstmember.book_name,"harry_potter");
    strcpy(firstmember.author_name,"J.K rowling");
    strcpy(firstmember.genre,"fiction");
    firstmember.pg_no=700;
    seondmember.library_id=102;
    strcpy(seondmember.book_name,"that night");
    strcpy(seondmember.author_name,"nidhi upadhya");
    strcpy(seondmember.genre,"murder mystery");
    seondmember.pg_no=500;
    thirdmember.library_id=103;
    strcpy(thirdmember.book_name,"the housemaid");
    strcpy(thirdmember.author_name,"fm");
    strcpy(thirdmember.genre,"thriller");
    thirdmember.pg_no=600;
    fourthmember.library_id=104;
    strcpy(fourthmember.book_name,"silent patient");
    strcpy(fourthmember.author_name,"alex");
    strcpy(fourthmember.genre,"thriller");
    fourthmember.pg_no=750;
    fifthmember.library_id=102;
    strcpy(fifthmember.book_name,"sherlock homes");
    strcpy(fifthmember.author_name,"arthur");
    strcpy(fifthmember.genre,"mystry");
    fifthmember.pg_no=900;


}