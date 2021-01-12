/*
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário 
          e mostre seu novo salário, com 15% de aumento

Resolução do problema:
*/

const input = require('readline-sync').question

let salario = Number(input('Informe seu sálario: R$'))

let salario_final = salario*1.15

console.log(`O salário final é ${salario_final.toFixed(2)}`)

