/*
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre 
          na tela o valor do seno, cosseno e tangente desse ângulo

Resolução do problema:
*/

const input = require('readline-sync').question

let graus = Number(input('Informe o angulo em graus: '))

let pi = Math.PI
let radianos = graus * (pi / 180)

let seno = Math.sin(radianos)
let cos = Math.cos(radianos)
let tan = Math.tan(radianos)

console.log(`Seno: ${seno.toFixed(4)}`);
console.log(`Cosseno: ${cos.toFixed(4)}`);
console.log(`Tangente: ${tan.toFixed(4)}`);