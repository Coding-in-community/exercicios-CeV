/*
Desafio 033

Problema: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var num1, num2, num3 int

func main(){
	fmt.Print("Digite o valor de num1: ")
	fmt.Scanln(&num1)
	fmt.Print("Digite o valor de num2: ")
	fmt.Scanln(&num2)
	fmt.Print("Digite o valor de num3: ")
	fmt.Scanln(&num3)

	maior := num1
	menor := num1

	if num2 > num1 && num2 > num3{
    	maior = num2
	}
	if num3 > num1 && num3 > num2{
    	maior = num3
	}


	if num2 < num1 && num2 < num3{
		menor = num2
	}
	if num3 < num1 && num3 < num2{
		menor = num3
	}

	fmt.Printf("O número %v é o maior.\n", maior)	
	fmt.Printf("O número %v é o menor.\n", menor)	
}
