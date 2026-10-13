#include<stdio.h>
#include <string.h>
int main()
{
    /* char name[7]="mishal";
     printf(name);

     char words[25];
     printf("\nenter the word:");
     scanf("%24s",words);

     char word[50]="aifa";
     printf("string: ");
     fgets(word,sizeof(word),stdin);
     printf("welcome,%s!\n",word);*/

    char word[50]="aifa ismail";
    for(int i=0;i<strlen(word);i++){
        printf("%c",word[i]);
    }
    return 0;
}