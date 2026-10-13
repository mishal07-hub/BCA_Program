#include <stdio.h>
int main(){
    int a,b;
    printf("enter  number:");
    scanf("%d",&a);
    printf("enter  number:");
    scanf("%d",&b);
    printf("sum=%d\n",a+b);
    printf("diff=%d\n",a-b);
    printf("product=%d\n",a*b);
    printf("quotient=%d\n",a/b);
    printf("modulus=%d\n",a%b);
    printf("-----------------------");
    float f1,f2;
    printf("\nenter  number:");
    scanf("%f",&f1);
    printf("enter number:");
    scanf("%f",&f2);
    printf("sum=%.2f\n",f1+f2);
    printf("diff=%.2f\n",f1-f2);
    printf("product=%.2f\n",f1*f2);
    printf("quotient=%.2f\n",f1/f2);
    printf("modulus=%d\n",(int)f1%(int)f2);
    printf("-----------------------");
    double d1,d2;
    printf("\nenter number:");
    scanf("%lf",&d1);
    printf("enter number:");
    scanf("%lf",&d2);
    printf("sum=%.2lf\n",d1+d2);
    printf("diff=%.2lf\n",d1-d2);
    printf("product=%.2lf\n",d1*d2);
    printf("quotient=%.2lf\n",d1/d2);
    printf("modulus=%d\n",(int)d1%(int)d2);
    printf("-----------------------");
    char c1,c2;
    printf("\nenter character:");
    scanf(" %c",&c1);
    printf("enter character:");
    scanf(" %c",&c2);
    printf("sum= %c+%c\n",c1,c2);
    printf("diff= %c-%c\n",c1,c2);
    printf("product= %c*%c\n",c1,c2);
    printf("quotient= %c/%c\n",c1,c2);
    printf("modulus= %c % (%c)\n",c1%c2);
    printf("-----------------------");
    return 0;

    
}