/*
    003 - Somando dois números
    Crie um script Python que leia dois números e tente mostrar a soma entre eles
*/

#include <stdio.h>

int main(void)
{
    int n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%i", &n1);

    printf("digite o segundo número: ");
    scanf("%i", &n2);

    printf("A soma entre os números digitados é: %i\n", n1 + n2);
    
    return 0;
}