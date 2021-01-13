/*
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Resolução do problema:
*/

package main

import(
	"fmt"
)

var dias, km, valor float64

func main(){
	fmt.Print("Digite a quantidade de dias: ")
	fmt.Scanln(&dias)
	fmt.Print("Digite os Km percorridos: ")
	fmt.Scanln(&km)

	valor = (dias * 60) + (km * 0.15)

	fmt.Println("O total a ser pago é", valor)
}
