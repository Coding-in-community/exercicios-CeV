/*
	Desafio: 005
	Problema: Faça um programa que leia um número inteiro 
	e mostre na tela o seu sucessor e seu antecessor
*/

package main 
import "fmt"

func main() {
	var number int
	var sucessor int 
	var predecessor int
	fmt.Print("Digite um número: ")
	fmt.Scan(&number)
	sucessor = number + 1
	predecessor = number - 1
	fmt.Println("Antecessor:", predecessor, "Número:", number, "Sucessor:" ,sucessor)
}