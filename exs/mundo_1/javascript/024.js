/*
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const cidade = input('Digite o nome da cidade: '.toLowerCase())
console.log(cidade.indexOf('santo') != -1 ) // Função indexOf é para saber se palavra que voce quer esta na frase.
