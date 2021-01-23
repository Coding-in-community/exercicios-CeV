/*
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

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
	fmt.Print("Digite o nome de uma cidade: ")
	cidade, _ := scanner.ReadString('\r')

	nomes := strings.Fields(cidade)

	if strings.ToUpper(nomes[0]) == "SANTO"{
		fmt.Println("Essa cidade começa com Santo!")
	} else{
		fmt.Println("Essa cidade não começa com Santo.")
	}
}
