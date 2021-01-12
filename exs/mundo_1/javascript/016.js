/*
Desafio 016

Problema: Crie um programa que leia um número real qualquer 
          pelo teclado e mostre na tela a sua porção inteira

Resolução do problema:
*/

const input = require('readline-sync').question

let num = Number(input('Informe um número flutuante: '))

console.log(Math.trunc(num));