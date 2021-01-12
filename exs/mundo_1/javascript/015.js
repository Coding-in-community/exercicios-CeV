/*
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

Resolução do problema:
*/

const input = require('readline-sync').question

let dia = Number(input('Dias alugado: '))
let km = Number(input('Km rodados: '))

let valor = (dia * 60) + (km * 0.15)

console.log(`Total a pagar R$${valor.toFixed(2)}`)