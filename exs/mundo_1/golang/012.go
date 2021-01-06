/*
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.

Resolução do problema:
*/

package main

import (
	"fmt"
)

func main(){
	var preco float64
	fmt.Print("Digite o preço do produto: ")
	fmt.Scanln(&preco)

	desconto := preco * 0.05 // 5% = 0.05
	precoComDesconto := preco - desconto
	fmt.Printf("O produto com %s de desconto, fica %.2f reais.", "5%", precoComDesconto)
}


