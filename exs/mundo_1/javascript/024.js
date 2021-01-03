const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const cidade = input('Digite o nome da cidade: '.toLowerCase())
console.log(cidade.indexOf('santo') != -1 ) // Função indexOf é para saber se palavra que voce quer esta na frase.
