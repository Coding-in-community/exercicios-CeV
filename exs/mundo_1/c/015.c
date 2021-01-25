/*
    015 - Aluguel de carros
        Escreva um programa que pergunte a quantidade de Km percorridos por um carro
        alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
        pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
*/

#include <stdio.h>

int main(void)
{
    int dias_rod;
    float km_rod, total;

    printf("Quantidade de dias rodados: ");
    scanf("%i", &dias_rod);

    printf("Quilômetros rodados: ");
    scanf("%f", &km_rod);

    total = (dias_rod * 60) + (km_rod * 0.15);
    printf("\nValor a pagar: R$%.2f\n", total);
    return 0;
}
