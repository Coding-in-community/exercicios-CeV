/*
    017 - Catetos e hipotenusa
        Faça um programa que leia o comprimento do cateto oposto (co) e do cateto
        adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da
        hipotenusa
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
    float cat_op, cat_ad, hipot;
    printf("Digite o valor do cateto oposto e do cateto adjacente separados por espaço: ");
    scanf("%f %f", &cat_op, &cat_ad);

    hipot = sqrt((cat_op * cat_op) + (cat_ad * cat_ad));
    printf("A hipotenusa mede: %.2f\n", hipot);
    return 0;
}
