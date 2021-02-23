/*
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var velocidade float64

func main(){
	fmt.Print("Digite a velocidade do carro: ")
	fmt.Scanln(&velocidade)

	if velocidade > 80{
		fmt.Println("Você foi multado!")
		multa := (velocidade - 80) * 7
		fmt.Printf("Sua multa foi de R$%v.\n", multa)
	} else {
		fmt.Println("Parabéns! Você está dirigindo na velocidade certa.")
	}
}
