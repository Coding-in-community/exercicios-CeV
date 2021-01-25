/*
    005 - Antecessor e sucessor
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("Digite um número: ");
    scanf("%i", &num);

    printf("O antecessor e sucessor do número digitado são, respectivamente, %i e %i\n", num - 1, num + 1);

    return 0;
}