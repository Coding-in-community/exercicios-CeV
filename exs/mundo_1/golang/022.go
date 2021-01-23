/*
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

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
	inputReader := bufio.NewReader(os.Stdin)
	fmt.Print("Digite seu nome: ")

	nome, _ := inputReader.ReadString('\r')
	nome = strings.TrimSuffix(nome, "\r")
	semEspacos := strings.ReplaceAll(nome, " ", "")

	nomes := strings.Fields(nome)
	primeiroNome := nomes[0]

	fmt.Print("Seu nome com todas as letras maiúsculas fica: ")
	fmt.Println(strings.ToUpper(nome))
	fmt.Print("Seu nome com todas as letras minúsculas fica: ")
	fmt.Println(strings.ToLower(nome))
	fmt.Printf("Seu nome sem espaços tem %v letras.\n", len(semEspacos))
	fmt.Printf("Seu primeiro nome tem %v letras.\n", len(primeiroNome))
}
