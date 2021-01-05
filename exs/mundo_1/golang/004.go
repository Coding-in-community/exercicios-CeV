/*
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
*/

package main

import(
	"fmt"
	"regexp"
	"reflect"
	"go/token"
	"strings"
)

var IsAlpha = regexp.MustCompile(`^[a-zA-Z]+$`).MatchString
var IsAlnum = regexp.MustCompile(`[[:alnum:]]`).MatchString
var IsNumeric = regexp.MustCompile(`\p{N}`).MatchString
var IsDigit = regexp.MustCompile(`[[:digit:]]`).MatchString
var IsLower = regexp.MustCompile(`[[:lower:]]`).MatchString
var IsUpper = regexp.MustCompile(`[[:upper:]]`).MatchString
var IsPrintable = regexp.MustCompile(`[[:print:]]`).MatchString
var IsSpace = regexp.MustCompile(`[[:space:]]`).MatchString

func IsCapitalized(s string) bool{
	if s == strings.Title(s){
		return true
	} else {
		return false
	}
}

func main(){
	var n string
	fmt.Print("Digite algo: ")
	fmt.Scanln(&n)
	fmt.Println("O tipo primitivo desse valor é:", reflect.TypeOf(n))
	fmt.Println("É um número?", IsNumeric(n))
	fmt.Println("É um valor alfanumérico?", IsAlnum(n))
	fmt.Println("É texto?", IsAlpha(n))
	fmt.Println("É um digito?", IsDigit(n))
	fmt.Println("É um identificador?", token.IsKeyword(n))
	fmt.Println("Está em letra minúscula?", IsLower(n))
	fmt.Println("Está em letra maiúscula?", IsUpper(n))
	fmt.Println("É uma tabela de impressão?", IsPrintable(n))
	fmt.Println("É um espaço?", IsSpace(n))
	fmt.Println("Está capitalizada?", IsCapitalized(n))
}