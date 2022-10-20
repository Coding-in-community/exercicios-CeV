/*
    008 - Measurement converter
        Write a program that reads a value in meters and displays it converted to centimeters and millimeters
*/

#include <stdio.h>

int main(void)
{
    float meters;
    printf("Digite uma medida em meters: ");
    scanf("%f", &meters);

    printf("%.1f meters(s) it's the same as %.1f centímeters(s)\n", meters, meters * 100);
    printf("%.1f meters(s) it's the same as %.1f milímeters(s)\n", meters, meters * 1000);
    return 0;
}
