/*
Desafio 014

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.

Resolução do problema:
*/

package main

import(
	"fmt"
)

var temp float64

func main(){
	fmt.Print("Digite uma temperatura em Celsius: ")
	fmt.Scanln(&temp)

	f := 1.8 * temp + 32

	fmt.Println(temp, "graus Celsius em Fahrenheit fica", f)
}
