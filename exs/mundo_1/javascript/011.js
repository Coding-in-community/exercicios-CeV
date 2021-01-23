/*
Desafio 011

Problema: Faça um programa que leia a largura e a algura de uma parede em metros, 
          calcule a sua área e a quantidade de tinta necessária para pintá-la, 
          sabendo que cada litro de tinta pinta uma área de 2m²

Resolução do problema:
*/

const input = require('readline-sync').question

let largura = Number(input('Informe a largura da parede: '))
let altura = Number(input('Informe a altura da parede: '))

let area = largura * altura
let qtndTinta = area / 2

console.log(`A parede tem uma área de ${area}m²`)
console.log(`Será necessário ${qtndTinta}L de tinta para pintar a parede`)