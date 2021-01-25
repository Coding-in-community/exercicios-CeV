/*
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.

Resolução do problema:
*/

package main


import(
	"fmt"
	"math/rand"
	"time"
)


var aluno string

func main(){
	var alunos  []string
	for i := 0; i < 4; i += 1{
		fmt.Print("Digite o nome do aluno: ")
		fmt.Scanln(&aluno)
		alunos = append(alunos, aluno)
	} 

	rand.Seed(time.Now().Unix())
	fmt.Println("O aluno escolhido foi o(a)", alunos[rand.Intn(len(alunos))])
}
