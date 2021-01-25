/*
    012 - Calculando descontos
        Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
        5% de desconto
*/

#include <stdio.h>

int main(void)
{
    float val_inicial, val_final;
    printf("Digite o valor para aplicar 5%% de desconto: R$");
    scanf("%f", &val_inicial);

    val_final = val_inicial * 0.95;

    printf("Valor com desconto: R$%.2f\n", val_final);
    return 0;
}
