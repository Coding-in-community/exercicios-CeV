/*
    016 - Breaking a number
        Create a program that reads any real number from the keyboard and displays the
        screen its entire portion
*/
#include <stdio.h>

int main(void)
{
    float num;
    printf("Enter a number with decimal places: ");
    scanf("%f", &num);

    printf("The integer part of the number %.2f is %i\n", num, (int) num);
    return 0;
}
