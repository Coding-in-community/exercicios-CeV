// crie um script que leia dois números e tente mostrar a soma entre eles

const input = require('readline-sync').question
const print = console.log

let num1 = Number(input('Digite o primeiro número: '))
let num2 = Number(input('O segundo, por favor: '))
let soma = (num1 + num2)

print(`A soma entre ${num1} e ${num2} é ${soma}`)