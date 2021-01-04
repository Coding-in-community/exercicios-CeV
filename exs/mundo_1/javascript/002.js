/*
Desafio 002

Problema: Faça um programa que leia o nome de uma pessoa e mostre
          uma mensagem de boas-vindas.

Resolução do problema:
*/

const input = require('readline-sync').question
const print = console.log

let nome = input('Qual seu nome? ')
print(`Prazer em conhecer você, ${nome}`)