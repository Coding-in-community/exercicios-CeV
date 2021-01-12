/*
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para 
          apagar o quadro. Faça um programa que ajude ele, lendo o 
          nome deles e escrevendo o do escolhido

Resolução do problema:
*/

const input = require('readline-sync').question

let nome1 = input('1º aluno(a): ')
let nome2 = input('2º aluno(a): ')
let nome3 = input('3º aluno(a): ')
let nome4 = input('4º aluno(a): ')

let indiceAleatorio = Math.floor(
    Math.random() * 4
)

let escolha = [nome1, nome2, nome3, nome4][indiceAleatorio]

console.log(`O aluno escolhido foi: ${escolha}`);