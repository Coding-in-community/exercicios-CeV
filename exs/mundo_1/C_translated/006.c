/*
    006 - Double, triple and square root
        Create an algorithm that reads a number and displays your double, your triple, and your
        square root
*/

#include <stdio.h>
#include <math.h>

int main(void)
{   
    int number;
    printf("Digite um número: ");
    scanf("%i", &number);

    printf("Double of %i is %i\n", number, number * 2);
    printf("triple of %i is %i\n", number, number * 3);
    printf("The square root of  %i is %.2f\n", number, sqrt(number));

    return 0;
}