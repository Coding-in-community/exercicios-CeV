/*
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

Resolução do problema:
*/
package main

import (
	"fmt"
	"strings"
)
var x string

func main() {
	fmt.Print("Digite uma palavra: ")
	fmt.Scanln(&x)
	x = strings.ToLower(x)
	c := strings.Count(x, "a")
	i := strings.Index(x, "a")
	l := strings.LastIndex(x, "a")
	fmt.Printf("Index da primeira letra \"A\": %v\n", i)
	fmt.Printf("Quantidade de letras \"A\": %v\n", c)
	fmt.Printf("Index da última letra \"A\": %v\n", l)
}
