/*
Desafio 020

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.

Resolução do problema:
*/

package main


import(
	"fmt"
	"math/rand"
	"time"
)


var aluno   string
var alunos  []string

func main(){
	for i := 0; i < 4; i += 1{
		fmt.Print("Digite o nome do aluno: ")
		fmt.Scanln(&aluno)
		alunos = append(alunos, aluno)
	} 

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(alunos), func(i, j int) { alunos[i], alunos[j] = alunos[j], alunos[i] })
	fmt.Println("A ordem de apresentação será: ", alunos)
}
