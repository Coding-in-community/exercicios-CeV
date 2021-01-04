/*
Desafio 006

Problema: Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada

Resolução do problema:
*/

const input = require('readline-sync').question

let num = Number(input('Insira um número inteiro: '))
let dobro = num*2
let triplo = num*3
let raizQuadrada = Math.sqrt(num)

console.log(`O dobro de ${num} é ${dobro}`)
console.log(`O triplo é ${triplo}`)
console.log(`E a raiz quadrada é ${raizQuadrada.toFixed(2)}`)
