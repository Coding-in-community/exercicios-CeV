/*
	Desafio: 006
	Problema: Crie um algoritmo que leia um número 
	e mostre o seu dobro, o seu triplo 
	e sua raiz quadrada.
*/

package main 
import (
	"fmt"
	"math"
)

func main(){
	var number float64
	var double float64
	var triple float64
	var root float64
	fmt.Print("Informe um número: ")
	fmt.Scan(&number)
	double = number * 2
	triple = number * 3
	root = math.Sqrt(number)
	fmt.Println("Dobro:", double)
	fmt.Println("Triplo:", triple)
	fmt.Println("Raiz:", root)
}