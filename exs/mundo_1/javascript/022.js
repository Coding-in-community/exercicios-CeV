/*
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const nome = input('Digite seu nome: ')

//Declarando os dados no console "Saida de dados"
console.log(`Nome em maiúsculo ${nome.toUpperCase()}`)//Letras Maiúsculas
console.log(`Nome em minúsculo ${nome.toLowerCase()}`)//Letras Minúsculas
console.log(`Quantidade de letras  = ${nome.length}`)//Qtde de letras
console.log(nome.slice(0, 5).length) // Quantidade de letras do primeiro nome