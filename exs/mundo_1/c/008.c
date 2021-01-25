/*
    008 - Conversor de medidas
        Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
*/

#include <stdio.h>

int main(void)
{
    float metros;
    printf("Digite uma medida em metros: ");
    scanf("%f", &metros);

    printf("%.1f metro(s) é igual a %.1f centímero(s)\n", metros, metros * 100);
    printf("%.1f metro(s) é igual a %.1f milímetro(s)\n", metros, metros * 1000);
    return 0;
}
