/*
Desafio 031

Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas.

Resolução do problema:
*/

const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
const dist = input("Qual distância percorrida?: ")

if(dist <= 200){
    let price = (dist * 0.50)
    console.log(`Preço da passagem: R$${price.toFixed(2)}`)
}
else {
    let price = (dist*0.45)
    console.log(`Preço da passagem: R$ ${price.toFixed(2)}`)
}