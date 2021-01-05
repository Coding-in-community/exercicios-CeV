/*
Desafio 011
Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados.
Resolução do problema:
*/

package main

import(
	"fmt"
)

func main(){
	var altura, largura float64
	fmt.Print("Digite a altura da parede: ")
	fmt.Scanln(&altura)
	fmt.Print("Digite a largura da parede: ")
	fmt.Scanln(&largura)
	metros := altura * largura
	quantidadeTinta := metros/2
	fmt.Printf("\nPara pintar uma parede com %.2f metros quadrados, são necessários %.2f litros de tinta.\n", metros, quantidadeTinta)

}