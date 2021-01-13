/*
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.

Resolução do problema:
*/

package main

import (
	"fmt"
)

var salario float64

func main(){
	fmt.Print("Digite o salário do funcionário: ")
	fmt.Scanln(&salario)

	aumento := 0.15 //15% de aumento
	salarioComAumento := salario + (salario * aumento)
	fmt.Println("O salário de", salario ,"com 15% de aumento fica",salarioComAumento)
}
