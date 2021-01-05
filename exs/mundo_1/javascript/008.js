/*
Desafio 008

Problema: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

Resolução do problema:
*/

const input = require('readline-sync').question

let metro = Number(input('Insira um valor em metros: '))

let centimetro = metro*100
let milimetro = metro*1000

console.log(`Metros: ${metro}m`)
console.log(`Centímetros: ${centimetro}cm`)
console.log(`Milímetros: ${milimetro}mm`)