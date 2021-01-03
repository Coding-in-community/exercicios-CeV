/*
Desafio 030

Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

let n = input("Descubra se o numero é par ou impar: ")

// O calculo n % 2 == 0 é para saber se o numero é "PAR", se não for a condição vai retornar impar.

if(n == n % 2 == 0) { 
    console.log("Esse numero é par")
} 
else {
    console.log("Esse numero é impar")
}