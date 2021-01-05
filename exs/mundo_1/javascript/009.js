/*
Desafio 009

Problema: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

Resolução do problema:
*/

const input = require('readline-sync').question

let num = Number(input('Insira um número inteiro: '))
let intNum = Math.trunc(num)

console.log(`${intNum} x 01 = ${intNum * 1}`)
console.log(`${intNum} x 02 = ${intNum * 2}`)
console.log(`${intNum} x 03 = ${intNum * 3}`)
console.log(`${intNum} x 04 = ${intNum * 4}`)
console.log(`${intNum} x 05 = ${intNum * 5}`)
console.log(`${intNum} x 06 = ${intNum * 6}`)
console.log(`${intNum} x 07 = ${intNum * 7}`)
console.log(`${intNum} x 08 = ${intNum * 8}`)
console.log(`${intNum} x 09 = ${intNum * 9}`)
console.log(`${intNum} x 10 = ${intNum * 10}`)
