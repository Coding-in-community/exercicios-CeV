/*
    003 - Adding two numbers
    Create a script that reads two numbers and tries to show the sum between them
*/
#include <stdio.h>

int main(void)
{
    int number1, number2;
    printf("Enter the first number: ");
    scanf("%i", &number1);

    printf("Enter the second number: ");
    scanf("%i", &number2);

    printf("The sum of the numbers entered is: %i\n", number1 + number2);
    
    return 0;
}