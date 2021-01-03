// crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

const input = require('readline-sync').question
const print = console.log

let nome = input('Qual seu nome? ')
print(`Prazer em conhecer você, ${nome}`)