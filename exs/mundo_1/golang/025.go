/*
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Resolução do problema:
*/

package main

import (
	"bufio"
	"fmt"
	"strings"
	"os"
)

func main(){
	scanner := bufio.NewReader(os.Stdin)
	fmt.Print("Digite seu nome: ")
	nome, _ := scanner.ReadString('\n')

	if strings.Contains(strings.ToUpper(nome), "SILVA"){
		fmt.Println("Seu nome tem Silva.")
	} else {
		fmt.Println("Seu nome não tem Silva.")
	}
}
