/*
	Desafio: 002
	Problema: Crie um script que leia o nome de uma 
	pessoa e mostre uma mensagem de boas-vindas de acordo com 
	o valor digitado
*/
package main
import "fmt"
func main() {
	var name string
	fmt.Println("Olá, qual seu nome?")
	fmt.Scanln(&name)
	fmt.Println("Bem vindo, " + name)
}