/*
	Desafio: 009
	Problema: Faça um programa que leia um número Inteiro qualquer
    e mostre na tela a sua tabuada.

*/

package main
import "fmt"

func main() {
	var value float64
	fmt.Print("Informe o valor: ")
	fmt.Scan(&value)
	fmt.Println(value, "X 0 =", value * 0)
	fmt.Println(value, "X 1 =", value * 1)
	fmt.Println(value, "X 2 =", value * 2)
	fmt.Println(value, "X 3 =", value * 3)
	fmt.Println(value, "X 4 =", value * 4)
	fmt.Println(value, "X 5 =", value * 5)
	fmt.Println(value, "X 6 =", value * 6)
	fmt.Println(value, "X 7 =", value * 7)
	fmt.Println(value, "X 8 =", value * 8)
	fmt.Println(value, "X 9 =", value * 9)
	fmt.Println(value, "X 10 =", value * 10)
}
