/*
    002 - Respondendo ao usuário
    Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de
    boas-vindas de acordo com o valor digitado
*/

#include <stdio.h>

int main(void)
{
    char nome[50];
    printf("Qual o seu nome? ");
    scanf("%s", &nome);
    printf("Seja bem-vindo, %s!\n", nome);
    return 0;
}