/*
	Desafio: 008
	Problema: Escreva um programa que leia um valor 
	em metros e o exiba convertido em centímetros 
	e milímetros.
*/

package main
import "fmt"

func main() {
	var meter float64
	var centimeter float64
	var millimeter float64
	fmt.Print("Informe o valor em metro(s): ")
	fmt.Scanln(&meter)
	centimeter = meter * 100
	millimeter = meter * 1000
	fmt.Println("Centímetro:", centimeter)
	fmt.Println("Milímetro:", millimeter)
}
