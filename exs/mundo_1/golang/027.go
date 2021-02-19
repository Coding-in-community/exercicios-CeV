/*
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

Resolução do problema:
*/

package main

import(
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main(){
	fmt.Print("Digite um nome completo: ")

	scanner := bufio.NewReader(os.Stdin)
	nome, err := scanner.ReadString('\r') 
	if err != nil{
		fmt.Fprintf(os.Stderr, "Name: %v\n", err)
	}

	x := strings.Fields(nome)
	lastName := len(x) -1
	fmt.Println(len(x))
	fmt.Printf("O primeiro nome é: %v\n", x[0])
	fmt.Printf("O último nome é: %v\n", x[lastName])
}
