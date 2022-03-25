// "Secure" Number Comparison
#include <stdio.h>

// function main begins program execution 
int main(void) {
    int num1 = 0; 
    int num2 = 0;
    puts("Enter two integers, and I will tell you");
    printf("the relationships they satisfy: ");
    scanf("%d", &num1); // read an integer
    scanf("%d", &num2); // read an integer
    
    puts("");
    if (num1 == num2) {
        printf("%d is equal to %d\n", num1, num2);
    } else {
        printf("%d is not equal to %d\n", num1, num2);
    }

    if (num1 > num2) {
        printf("%d is greater than %d\n", num1, num2);
        
    } else if (num1 < num2) {
        printf("%d is less than %d\n", num1, num2);
    }

    if (num1 >= num2) {
        printf("%d is greater than or equal to %d\n", num1, num2);
        
    } else if (num1 <= num2) {
        printf("%d is less than or equal to %d\n", num1, num2);
    }
    

} // end function main