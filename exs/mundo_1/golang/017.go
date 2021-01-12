/*
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.

Resolução do problema:
*/

package main

import (
	"fmt"
	"math"
)

var catOP, catAD float64

func main(){
	fmt.Print("Digite o valor do cateto adjacente: ")
	fmt.Scanln(&catAD)
	fmt.Print("Digite o valor do cateto oposto: ")
	fmt.Scanln(&catOP)

	hipotenusa := math.Hypot(catAD, catOP)

	fmt.Println("O valor da hipotenusa é igual a", hipotenusa)

}
