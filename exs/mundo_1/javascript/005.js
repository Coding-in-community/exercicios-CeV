/*
Desafio 005

Problema: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

Resolução do problema:
*/

const input = require('readline-sync').question

let num = Number(input('Insira um número inteiro: '))
let intNum = Math.round(num)

console.log(`O numero digitado foi ${intNum}`)
console.log(`Seu antecessor é ${intNum - 1} e o sucessor ${intNum + 1}`)
