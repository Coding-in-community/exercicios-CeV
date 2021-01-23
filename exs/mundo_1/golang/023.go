/*
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Resolução do problema:
*/
package main

import (
	"fmt"
)

var num, u, d, c, m int 


func main(){
	fmt.Print("Digite um número de 0 a 9999: ")
	fmt.Scanln(&num)

	u = num / 1 % 10
	d = num / 10 % 10
	c = num / 100 % 10
	m = num / 1000 % 10

	fmt.Printf("Unidades: %v, Dezenas: %v, Centenas: %v, Milhares: %v.", u, d, c, m)
}
