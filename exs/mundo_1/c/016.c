/*
    016 - Quebrando um número
        Crie um programa que leia um número real qualquer pelo teclado e mostre na
        tela a sua porção inteira
*/

#include <stdio.h>

int main(void)
{
    float num;
    printf("Digite um número com casas decimais: ");
    scanf("%f", &num);

    printf("A parte inteiro do número %.2f é %i\n", num, (int) num);
    return 0;
}
