/*
Desafio 014

Problema: Conversor de temperaturas: escreva um programa que converta uma temperatura 
          digitada em ºC para ºF

Resolução do problema:
*/

const input = require('readline-sync').question

let temperatura_C = Number(input('Informe a temperatura em °C: '))

let temperatura_F = 1.8 * temperatura_C + 32

console.log(`Temperatura: ${temperatura_F.toFixed(1)}°F`)
