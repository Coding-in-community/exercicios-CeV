/*
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.

Resolução do problema:
*/

package main

import (
    "fmt"
    "math/rand"
    "time"
)

var chute int

func main() {
    rand.Seed(time.Now().UnixNano())
    n := rand.Intn(5)
    fmt.Println("Estou pensando em um número de 0 a 5.")
    fmt.Println("Tente adivinhar!")
    fmt.Print("Digite seu palpite: ")
    fmt.Scanln(&chute)

    if chute == n{
    	fmt.Println("ACERTOU!")
    } else{
    	fmt.Println("ERROU!")
    	fmt.Printf("O número que pensei foi %v\n", n)
    }

}
