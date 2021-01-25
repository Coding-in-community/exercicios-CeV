/*
    006 - Dobro, triplo e raiz quadrada
        Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua
        raiz quadrada
*/

#include <stdio.h>
#include <math.h>

int main(void)
{   
    int num;
    printf("Digite um número: ");
    scanf("%i", &num);

    printf("O dobro de %i é %i\n", num, num * 2);
    printf("O triplo de %i é %i\n", num, num * 3);
    printf("A raiz quadrada de %i é %.2f\n", num, sqrt(num));

    return 0;
}