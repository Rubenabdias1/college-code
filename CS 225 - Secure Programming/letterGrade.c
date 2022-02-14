// Addition program.
#include <stdio.h>

// function main begins program execution 
int main(void) {
    int grade = 0; // will hold the grade user enters 
 
    printf("Enter the grade: "); // prompt
    scanf("%d", &grade); // read an integer
    if (grade > 100) {
        puts("The grade is greater than 100");
    }
    
    if (grade < 0) {
        puts("The grade is les than 0");
    }
    
    if (grade >= 90) {
        puts("A");
    } // end if
    else if (grade >= 80) {
        puts("B");
    } // end else if
    else if (grade >= 70) {
        puts("C");
    } // end else if
    else if (grade >= 60) {
        puts("D");
    } // end else if
    else {
        puts("F");
    } // end else

} // end function main