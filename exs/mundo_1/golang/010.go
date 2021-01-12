/*
	Desafio: 010
	Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
    na carteira e mostre quantos dólares ela pode comprar.

*/

package main
import (
	"fmt"
)

func main() {
	var real float64
	fmt.Print("Informe um valor: R$")
	fmt.Scanln(&real)
	dol := 5.24
	resultado := float64(real) / float64(dol)
	fmt.Printf("Você pode comprar U$%.2f", resultado)

}
