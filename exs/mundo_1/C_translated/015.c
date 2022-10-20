/*
    015 - Car rent
        Write a program that asks the number of kilometers traveled by a car
        rented and the number of days for which it was rented. Calculate the price at
        pay, knowing that the car costs R$ 60 per day and R$ 0.15 per km driven
*/

#include <stdio.h>

int main(void)
{
    int rotated_days;
    float rotated_kilometers, total;

    printf("Amount of rotated days: ");
    scanf("%i", &rotated_days);

    printf("Rotated Kilometers: ");
    scanf("%f", &rotated_kilometers);

    total = (rotated_days * 60) + (rotated_kilometers * 0.15);
    printf("\nValue to pay: R$%.2f\n", total);
    return 0;
}
