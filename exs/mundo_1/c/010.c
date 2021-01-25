/*
    010 - Conversor de moedas
        Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
        quantos dólares ela pode comprar
*/

#include <stdio.h>

int main(void)
{
    double dinh_cart;
    printf("Digite a quantia de dinheiro que você possui: R$");
    scanf("%lf", &dinh_cart);

    printf("Com R$%.2lf você pode comprar %.2lf dólares\n", dinh_cart, dinh_cart / 5.2);
    return 0;
}
