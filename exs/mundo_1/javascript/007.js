/*
Desafio 007

Problema: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

Resolução do problema:
*/

const input = require('readline-sync').question

let nota1 = Number(input('A primeira nota foi: '))
let nota2 = Number(input('E a segunda: '))
let media = (nota1 + nota2) / 2

console.log(`A média entre ${nota1} e ${nota2} é ${media.toFixed(2)}`)
