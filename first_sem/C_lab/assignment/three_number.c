#include<stdio.h>
int main()
{
    int a,b,c ;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    /*largest number*/
    if (a>b && a>c)
    {
        printf("%d is the Largest number\n", a);
    }
    else if (b>a && b>c)
    {
        printf("%d is the Largest Number\n", b);
    }
    else
    {
        printf("%d is the Largest Number\n", c);
    }

    /*smallest number*/
    if (a<b && a<c)
    {
        printf("%d is the smallest number", a);
    }
    else if (b<a && b<c)
    {
        printf("%d is the smallest Number", b);
    }
    else
    {
        printf("%d is the smallest Number", c);
    }
    return 0;
}
