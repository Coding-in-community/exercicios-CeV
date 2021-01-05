/*
Desafio 010

Problema: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

Resolução do problema:
*/

const input = require('readline-sync').question

let qntDinheiro = Number(input("Quanto dinheiro você tem? R$"))
let valorDolar = 5.65

let qntDolar = (qntDinheiro / valorDolar)

console.log(`Você pode comprar U$${qntDolar.toFixed(2)}`)
