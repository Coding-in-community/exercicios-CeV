/*
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.

Resolução do problema:
*/

package main

import(
	"fmt"
	"math"
)

var ang float64

func main(){
	fmt.Print("Digite o valor do ângulo: ")
	fmt.Scanln(&ang)

	cos := math.Cosh(ang)
	sin := math.Sin(ang)
	tan := math.Tan(ang)

	fmt.Printf("O seno do ângulo de %.2f graus é igual a %.2f.\n", ang, sin)
	fmt.Printf("O cosseno do ângulo de %.2f graus é igual a %.2f.\n", ang, cos)
	fmt.Printf("A tangente do ângulo de %.2f graus é igual a %.2f.\n", ang, tan)

}
