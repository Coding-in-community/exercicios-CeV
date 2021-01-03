const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const num = input('Digite um numero')

//Fazendo os calculos dos digitos
let u = num / 1 % 10
let d = num / 10 % 10
let c = num / 100 % 10
let m = num / 1000 % 10

//Imprimindo no console
console.log(`Unidade ${u.toFixed(0)}`) //toFixed é para tirar as casas decimais
console.log(`Dezena ${d.toFixed(0)}`)
console.log(`Centena ${c.toFixed(0)}`)
console.log(`Milhar ${m.toFixed(0)}`)
