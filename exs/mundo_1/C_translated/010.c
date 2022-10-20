/*
    010 - Currency converter
        Create a program that reads how much money a person has in their wallet and shows
        how many dollars can she buy
*/

#include <stdio.h>

int main(void)
{
    double money;
    printf("Enter the amount of money you have: $");
    scanf("%lf", &money);

    printf("Whith $%.2lf dolars you can buy %.2lf R$\n", money, money * 5.2);
    return 0;
}
