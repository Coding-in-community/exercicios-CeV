/*
    014 - Temperature converter
        Temperature Converter: Write a program that converts a temperature
        typed in °C to °F
*/

#include <stdio.h>

int main(void){
    float temperature_degrees;
    printf("Enter the temperature in degrees to be converted: ");
    scanf("%f", &temperature_degrees);

    printf("Conversion to Fahrenheit: %.1f°F\n", temperature_degrees * 1.8 + 32);
    return 0;
}
