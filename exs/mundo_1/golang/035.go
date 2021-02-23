/*
Desafio 035

Problema: Desenvolva um programa que leia o comprimento de três
          retas e diga ao usuário se elas podem ou não formar um triângulo.

Resolução do problema:
*/

package main

import (
	"fmt"
	"math"
)

var lado_A, lado_B, lado_C float64
var analise bool

func main(){
	fmt.Print("Digite o valor do lado A: ")
	fmt.Scanln(&lado_A)
	fmt.Print("Digite o valor do lado B: ")
	fmt.Scanln(&lado_B)
	fmt.Print("Digite o valor do lado C: ")
	fmt.Scanln(&lado_C)

	if math.Abs(lado_B - lado_C) < lado_A && lado_A < (lado_B + lado_C) {
		if math.Abs(lado_A - lado_C) < lado_B && lado_B < (lado_A + lado_C){
		    if math.Abs(lado_A - lado_B) < lado_C && lado_C < (lado_A + lado_B){
		        analise = true	
		    }
		}
	}
	if analise{
	    fmt.Println("As retas PODEM FORMAR um triângulo.")
	} else {
	    fmt.Println("As retas NÃO PODEM FORMAR um triângulo.")
	}
}
