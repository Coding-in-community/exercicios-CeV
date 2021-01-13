/*
Desafio 016

Problema: Crie um programa que leia um número Real qualquer
          pelo teclado e mostre na tela a sua porção Inteira.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var n float64

func main(){
	fmt.Print("Digite um número real: ")
	fmt.Scanln(&n)
	fmt.Println("A porção inteira de", n ,"é", int(n))
}
