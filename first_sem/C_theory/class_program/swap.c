include<stdio.h>

void swap(int *a, int *b){
    int temp; 

    temp = *a;     // save the value at address a 
    *a = *b;       // put the value at address b into address a 
    *b = temp;     // put the saved value into address b 
}

int main(){
    int x, y;

    printf("Enter first number: ");
    scanf("%d", &x);
    
    printf("Enter second number: ");
    scanf("%d", &y);

    printf("\nBefore swapping: x = %d, y = %d\n", x, y);

    swap(&x, &y);      // send the addresses of x and y 

    printf("After swapping:  x = %d, y = %d\n", x, y);

    return 0;
}