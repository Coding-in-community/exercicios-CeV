/*
    009 - Multiplication table
        Write a program that reads any integer and displays its
        multiplication table
*/

#include <stdio.h>

int main(void)
{
    int number;
    printf("Enter the number you want to see the multiplication table: ");
    scanf("%i", &number);

    printf("==================\n");
    printf("%i x %i  = %i\n", number, 1, number * 1);
    printf("%i x %i  = %i\n", number, 2, number * 2);
    printf("%i x %i  = %i\n", number, 3, number * 3);
    printf("%i x %i  = %i\n", number, 4, number * 4);
    printf("%i x %i  = %i\n", number, 5, number * 5);
    printf("%i x %i  = %i\n", number, 6, number * 6);
    printf("%i x %i  = %i\n", number, 7, number * 7);
    printf("%i x %i  = %i\n", number, 8, number * 8);
    printf("%i x %i  = %i\n", number, 9, number * 9);
    printf("%i x %i = %i\n", number, 10, number * 10);
    printf("==================\n");
    
    return 0;
}
