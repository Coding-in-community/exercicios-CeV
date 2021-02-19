/*
Desafio 032

Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Resolução do problema:
*/

package main

import(
	"fmt"
	"time"
)

var ano int

func main(){
	fmt.Prtin("Digite um ano: ")
	fmt.Scanln(&ano)

	if ano == 0{
		ano = time.Now().Year()
	}

	if ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0{
		fmt.Printf("O ano %v é bissexto.\n", ano)
	} else {
		fmt.Printf("O ano %v não é bissexto.\n", ano)
	}
}
