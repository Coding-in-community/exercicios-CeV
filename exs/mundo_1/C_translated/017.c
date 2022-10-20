/*
    017 - Pecacary and hypotenuse
        Write a program that reads the length of the opposite side (co) and the side
        adjacent (ca) of a right triangle, calculate and display the length of the
        hypotenuse
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
    float oposit_peccary, adjacent_pecarry, hypot;
    printf("Enter the value of the opposite and adjacent sides separated by a space: ");
    scanf("%f %f", &oposit_peccary, &adjacent_pecarry);

    hypot = sqrt((oposit_peccary * oposit_peccary) + (adjacent_pecarry * adjacent_pecarry));
    printf("The hypotenuse measures: %.2f\n", hypot);
    return 0;
}
