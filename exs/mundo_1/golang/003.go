/*
	Desafio: 003
	Problema: Crie um script Python que leia dois números
	e tente mostrar a soma entre eles
*/

package main

import "fmt"

func main() {
	var first float64
	var second float64
	fmt.Print("Primeiro Número: ")
	fmt.Scan(&first)
	fmt.Print("Segundo Número: ")
	fmt.Scan(&second)
	fmt.Println(first + second)
}
