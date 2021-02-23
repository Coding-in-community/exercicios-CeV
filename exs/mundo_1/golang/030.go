/*
Desafio 030

Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var n int 

func main(){
	fmt.Print("Digite um número inteiro: ")
	fmt.Scanln(&n)

	if n % 2 == 0{
		fmt.Printf("O número %v é par.\n", n)
	} else {
		fmt.Printf("O número %v é ímpar.\n", n)
	}
}
