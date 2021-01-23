/*
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e 
          mostre seu novo preço, com 5% de desconto

Resolução do problema:
*/

const input = require('readline-sync').question

let preco = Number(input('Informe o preço do produto: R$'))

total = preco*0.95

console.log(`Total à pagar com 5% de desconto: R$${total.toFixed(2)}`)