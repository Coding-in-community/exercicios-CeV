/*
    012 - Calculating discounts
        Make an algorithm that reads the price of a product and displays its new price, with
        5% off
*/
#include <stdio.h>

int main(void)
{
    float inicial_value, final_value;
    printf("Enter the value to apply 5%% of discount: $");
    scanf("%f", &inicial_value);

    final_value = inicial_value * 0.95;

    printf("Value whith discount: $%.2f\n", final_value);
    return 0;
}
