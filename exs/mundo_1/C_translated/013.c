/*
    013 - Salary readjustment
        Make an algorithm that reads an employee's salary and displays his new
        salary, with a 15% increase
*/

#include <stdio.h>

int main(void)
{
    float Inicial_salary;
    printf("Enter salary to calculate salary increase of 15%%: $");
    scanf("%f", &Inicial_salary);

    printf("Salary with increase: $%.2f\n", Inicial_salary * 1.15);
    return 0;
}
