/*
    011 - Painting wall
        Write a program that reads the width and height of a wall in meters,
        calculate its area and the amount of paint needed to paint it, knowing
        that each liter of paint paints an area of ​​2m²
*/

#include <stdio.h>

int main(void)
{
    float heigth, width;
    printf("Enter the height and width, in meters, of the wall separated by space: ");
    scanf("%f %f", &heigth, &width);

    float area = heigth * width;

    printf("To paint %.2fm² of wall it's necessary %.1f liters of ink\n", area, area / 2);
    return 0;
}
