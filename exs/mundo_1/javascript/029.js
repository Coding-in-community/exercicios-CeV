/*
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados 
let velo = input("Velocidade do carro: ")

// Verificando se a velocidade esta acima do limite com if e else
if(velo > 80){
    console.log(`Você está acima do limite permitido! Velocidade de ${velo}`)
    let multa = 7 * (velo-80)
    console.log(`Sua multa é de ${multa.toFixed(2)} `)
}
else {
    console.log("Velocidade dentro do limite. Boa viagem.")
}