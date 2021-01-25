/*
    011 - Pintando parede
        Faça um programa que leia a largura e a algura de uma parede em metros,
        calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
        que cada litro de tinta pinta uma área de 2m²
*/

#include <stdio.h>

int main(void)
{
    float alt, larg;
    printf("Digite a altura e a largura, em metros, da parede separados por espaço: ");
    scanf("%f %f", &alt, &larg);

    float area = alt * larg;

    printf("Para pintar %.2fm² de parede é necessário %.1f litros de tinta\n", area, area / 2);
    return 0;
}
