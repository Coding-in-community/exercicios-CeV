/*
    013 - Reajuste salarial
        Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
        salário, com 15% de aumento
*/

#include <stdio.h>

int main(void)
{
    float sal_inicial;
    printf("Digite o salário para calcular o aumento de 15%%: R$");
    scanf("%f", &sal_inicial);

    printf("Salário com aumento: R$%.2f\n", sal_inicial * 1.15);
    return 0;
}
