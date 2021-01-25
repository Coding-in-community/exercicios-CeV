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
    for (int i = 0; i <= 10; i++)
    {
        printf("%i x %i", num, i);
        
        // alinha os sinais de igualdade
        if (i < 10)
        {
            printf("  ");
        }
        else
        {
            printf(" ");
        }

        printf("= %i\n", num * i);
    }
    printf("==================\n");
    
    return 0;
}
