/*
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto (co) e 
          do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre 
          o comprimento da hipotenusa

Resolução do problema:
*/

const input = require('readline-sync').question

let cateto_oposto = Number(input('Informe o cateto oposto: '))
let cateto_adjacente = Number(input('Informe o cateto adjacente: '))

let hipotenusa = Math.hypot(cateto_oposto, cateto_adjacente)

console.log(`Hipotenusa: ${hipotenusa}`);