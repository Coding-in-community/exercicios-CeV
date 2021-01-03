/*
Desafio 033

Problema: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
let n1 = input("Digite um primeiro número: ")
let n2 = input("Digite um segundo número: ")
let n3 = input("Digite um terceiro e último número: ")



let max = Math.max(n1, n2, n3); //Recomendo pesquisa sobre a max e min no doc do javascript.
let min = Math.min(n1, n2, n3);

console.log(`Maior numero é ${max}`)
console.log(`Menor numero é ${min}`)
