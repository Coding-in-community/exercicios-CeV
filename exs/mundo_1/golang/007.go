/*
	Desafio: 007
	Problema: Desenvolva um programa que leia 
	as duas notas de um aluno, calcule e 
	mostre a sua média.
*/

package main 
import (
	"fmt"
)

func main(){
	var first float64
	var second float64
	var calc float64
	fmt.Print("Informe a primeira nota: ")
	fmt.Scanln(&first)
	fmt.Print("Informe a segunda nota: ")
	fmt.Scanln(&second)
	calc = first + second / 2
	fmt.Print("Média: ", calc)
}