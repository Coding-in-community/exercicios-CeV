/*
    009 - Tabuada
        Faça um programa que leia um número inteiro qualquer e mostre na tela a sua
        tabuada
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("Digite o número que você quer ver a tabuada: ");
    scanf("%i", &num);

    printf("==================\n");
    printf("%i x %i  = %i\n", num, 1, num * 1);
    printf("%i x %i  = %i\n", num, 2, num * 2);
    printf("%i x %i  = %i\n", num, 3, num * 3);
    printf("%i x %i  = %i\n", num, 4, num * 4);
    printf("%i x %i  = %i\n", num, 5, num * 5);
    printf("%i x %i  = %i\n", num, 6, num * 6);
    printf("%i x %i  = %i\n", num, 7, num * 7);
    printf("%i x %i  = %i\n", num, 8, num * 8);
    printf("%i x %i  = %i\n", num, 9, num * 9);
    printf("%i x %i = %i\n", num, 10, num * 10);
    printf("==================\n");
    
    return 0;
}
