/*
Desafio 003

Problema: Crie um programa que leia dois números e mostre a soma entre eles.

Resolução do problema:
*/

const input = require('readline-sync').question
const print = console.log

let num1 = Number(input('Digite o primeiro número: '))
let num2 = Number(input('O segundo, por favor: '))
let soma = (num1 + num2)

print(`A soma entre ${num1} e ${num2} é ${soma}`)