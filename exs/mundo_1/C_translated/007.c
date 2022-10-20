/*
    007 - Arithmetic average
       Develop a program that reads a student's two grades, calculates and displays the
        average
*/

#include <stdio.h>

int main(void)
{
    float grade[2];

    printf("Write the first grade: ");
    scanf("%f", &grade[0]);

    printf("Write the second grade: ");
    scanf("%f", &grade[1]);

    printf("The student average is %.2f\n", (grade[0] + grade[1]) / 2);
    return 0;
}
