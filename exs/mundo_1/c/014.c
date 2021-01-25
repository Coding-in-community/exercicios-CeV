/*
    014 - Conversor de temperaturas
        Conversor de temperaturas: escreva um programa que converta uma temperatura
        digitada em ºC para ºF
*/

#include <stdio.h>

int main(void){
    float temp_graus;
    printf("Digite a temperatura em graus a ser convertida: ");
    scanf("%f", &temp_graus);

    printf("Conversão para Fahrenheit: %.1f°F\n", temp_graus * 1.8 + 32);
    return 0;
}
