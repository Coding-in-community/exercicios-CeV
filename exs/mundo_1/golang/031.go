/*
Desafio 031

Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas.

Resolução do problema:
*/

package main

import(
	"fmt"
)

var d, preco float64

func main(){
	fmt.Print("Digite a distância em KM: ")
	fmt.Scanln(&d)

	if d > 200{
		preco = d * 0.45
	} else {
		preco = d * 0.50
	}

	fmt.Printf("Para %vKM, o preço fica R$%v.\n", d, preco)
}
