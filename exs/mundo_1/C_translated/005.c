/*
    005 - Predecessor and successor
    Write a program that reads an integer and displays its successor and predecessor on the screen
*/

#include <stdio.h>

int main(void)
{
    int number;
    printf("Write a number: ");
    scanf("%i", &number);

    printf("The predecessor and successor of the entered number are respectively, %i e %i\n", number - 1, number + 1);

    return 0;
}