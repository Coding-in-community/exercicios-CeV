const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const nome = input('Digite seu nome: ')

//Saida de dados
console.log(nome.indexOf('Silva') != -1)