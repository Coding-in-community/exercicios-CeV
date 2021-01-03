/*
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const frase = input('Digite uma frase: '.toUpperCase())

//Quantidade de letra "a"
console.log(`Quantidade de letra "A" ${frase.match(/a/g)}`)

//# Em que posição ela aparece a primeira vez
console.log(frase.indexOf("a",1)) // Aqui vocẽ tem que colocar a posição da letra

// Em que posição ela aparece a última vez
console.log(frase.indexOf("a", 2)) // Aqui vocẽ tem que colocar a posição da letra