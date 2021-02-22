/*
Desafio 034

Problema: Escreva um programa que pergunte o salário de um funcionário
          e calcule o valor do seu aumento. Para salários superiores a
          R$1250,00, calcule um aumento de 10%. Para os inferiores ou
          iguais, o aumento é de 15%.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var salario, aumento float64

func main(){
	fmt.Print("Digite seu salário: ")
	fmt.Scanln(&salario)

	if salario <= 1250{
		aumento = (salario * 1.15)
	} else {
		aumento = (salario * 1.10)
	}

	fmt.Printf("O salário com aumento fica R$%v.\n", aumento)
}
