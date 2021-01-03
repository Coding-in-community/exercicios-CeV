/*
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const nome = input('Digite seu nome: ')

//Saida de dados
console.log(nome.indexOf('Silva') != -1)