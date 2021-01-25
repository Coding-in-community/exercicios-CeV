/*
    007 - Média aritmética
        Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a
        sua média
*/

#include <stdio.h>

int main(void)
{
    float notas[2];

    printf("Digite a primeira nota: ");
    scanf("%f", &notas[0]);

    printf("Digite a segunda nota: ");
    scanf("%f", &notas[1]);

    printf("A média do aluno é %.2f\n", (notas[0] + notas[1]) / 2);
    return 0;
}
